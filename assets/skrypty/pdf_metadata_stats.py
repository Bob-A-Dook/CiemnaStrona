'''
! This script's code is mostly in English, but the displayed messages
  are in Polish.

My script used for analyzing metadata contained within PDF-format
issues of "Monitor Sądowy i Gospodarczy" (an official government
periodical with regular updates on a large subset of Polish companies).
Could also be useful for summarizing PDF metadata in general.
At its core, it's a wrapper around Poppler's pdfinfo.

At the end of the script, you can change the default settings.
'''
__author__ = 'Bob Adook'
__mail__ = 'bob.adook@tutanota.com'
__license__ = 'MIT'

# ^ In short: just use it however you want ;) No strings attached.
# However, I take no responsibility for anything you do.

import re
from pathlib import Path
from sys import modules
from subprocess import getoutput
from collections import Counter
from logging import error, basicConfig
from shutil import which as get_program_path
from platform import system
from code import interact
from multiprocessing import Pool, cpu_count

###########################
# Setup, mainly for pdfinfo
###########################

def _find_pdfinfo():
    '''
    Looks for a PDF metadata getter ("pdfinfo" from Poppler suite), 
    either in PATH or recursively in the script's folder.
    '''
    # First, check if it's available on system PATH
    pdfinfo_path = get_program_path('pdfinfo')
    if pdfinfo_path: return pdfinfo_path

    # If no program on PATH, search in the same folder as this script
    files = [f.absolute() for f in Path(__file__).parent.rglob('*')
             if 'pdfinfo' in f.name]
    if files: return str( files[0] )

    # If nothing works, show potential solutions to the user
    user_system = system()
    solutions = {
        'Windows': ('pobierz zipa z adresu:\nhttps://github.com/oschwartz10612'
                    '/poppler-windows/releases/download/v21.10.0-0/'
                    'Release-21.10.0-0.zip\ni rozpakuj go w tym samym'
                    ' folderze co ten skrypt.'),
        'Darwin': ('postępuj zgodnie z instrukcjami z:\n'
                   'https://macappstore.org/poppler/'),
        'Linux': ('wykonaj instrukcje z pierwszej odpowiedzi:\n'
                  'https://stackoverflow.com/questions/32156047/'
                  'how-to-install-poppler-in-ubuntu-15-04')}

    error('Nie znaleziono programu "pdfinfo"!')
    try: error( f'Aby go zdobyć, {solutions[user_system]}\n\n' )
    except KeyError:
        error('Nie mam gotowych rozwiązań dla tego systemu operacyjnego. '
              'Ale musisz w jakiś sposób zainstalować bibliotekę Poppler.\n')
    return None

PDFINFO_PATH = _find_pdfinfo()

RUNS_IN_IDLE = ('idlelib' in modules)
if RUNS_IN_IDLE:
    print('[UWAGA]\nSkrypt uruchomiono w edytorze IDLE. W takim wypadku '
          'nie będzie możliwe użycie wszystkich rdzeni procesora '
          '(edytor się nie lubi z biblioteką "multiprocessing").\n'
          'Jeśli chcesz pełnej szybkości, uruchom skrypt przez konsolę.\n')

basicConfig( format='[%(levelname)s] %(message)s' )

#############################
# Launching pdfinfo via shell
#############################

def _call_pdfinfo( file ):
    '''
    Uses the "pdfinfo" program to get a list of attributes and values
    describing a specific PDF file.
    '''
    out = getoutput( f'{PDFINFO_PATH} "{file}"' )
    lines = [l for l in out.split('\n') if l]
    return file, lines
    
                
def _get_pdfinfo_data_sequential( files ):
    '''Slower fallback version of getting data for multiple files'''
    return [ _call_pdfinfo( file ) for file in files]


def _get_pdfinfo_data_parallel( files ):
    '''Faster, multicore version of getting data for multiple files'''    
    with Pool( processes=cpu_count() ) as pool:
        all_data = pool.map( _call_pdfinfo, files )
    return all_data

#######################################
# General function for storing metadata
#######################################

def _get_metadata_from_pdfs( monitors ):
    '''Gets selected metadata fields from all Monitors.'''

    print(f'\n### Ładowanie statystyk dla {len(monitors)} Monitorów. '
          'Może to chwilę potrwać...\n')
    
    if RUNS_IN_IDLE or not USE_MULTIPROCESSING:
        raw_data = _get_pdfinfo_data_sequential( monitors )
    else:
        raw_data = _get_pdfinfo_data_parallel( monitors )
        
    regex_template = '^(.*?):\s+(.*?)$' # Field name, : and spaces, value
    field_regex = re.compile( regex_template )
    number_regex = re.compile('[0-9]+')
    pdf_regex = re.compile('(\d+)_\d+\.pdf')

    if USE_ON_MONITORS_ONLY:
        get_year = lambda name: pdf_regex.search( m_name ).group(1)
    else:
        get_year = lambda name: None

    all_monitor_info = []
    field_names = set()
    year_error_n = 0
    
    for file, lines in raw_data:

        m_name = file.name
        try: m_year = get_year( m_name )
        except Exception:
            m_year = 0
            year_error_n += 1
            
        monitor_object = PDFMetadata( m_name, m_year )

        for line in lines:
            try: attr, value = field_regex.search( line ).groups()
            except Exception:
                error(f'Błędny format danych z programu "pdfinfo":\n{line}')
                continue

            if attr == 'Title' and USE_ON_MONITORS_ONLY:
                # Special case; standardize numbers, keep all else
                value = number_regex.sub( '@', value )

            monitor_object[attr] = value
            field_names.add( attr )
    
        all_monitor_info.append( monitor_object )

    if year_error_n:
        error(f'\nZ nazw części plików ({year_error_n}) nie odczytano roku. '
              'Być może nie mają nazw typowych dla Monitorów. Jeśli używasz '
              'skryptu na innych plikach PDF, najlepiej ustaw wartość '
              'USE_ON_MONITORS_ONLY pod koniec skryptu na False\n')
        
    return all_monitor_info, list(field_names)


class PDFMetadata(dict):
    '''The class used for storing various labelled pieces of metadata'''
        
    def __init__( self, name, year ):
        self.name = name
        self.year = year

    def __missing__(self, key ):
        return 'BRAK DANYCH'

    def __repr__(self):
        text = '\n'.join( f'{k}: {v}' for (k,v) in self.items())
        return f'[{self.name}]\n{text}\n'

###################################
# Formatting and displaying results
###################################

def _get_value( monitor, field_name):
    try: value = monitor[field_name] 
    except Exception: value = 'BRAK DANYCH'
    return value


def _count_values( monitor_data, field_name ):
    '''Counts the total number of values of a specific metadata field'''
    
    matching_monitors = [(m.year, _get_value(m, field_name))
                         for m in monitor_data]

    count = {}         
    for year, value in matching_monitors:        
        try: count[ value ].append( year )
        except KeyError: count[ value ] = [year]

    count = [(value, len(years), min(years), max(years) )
             for (value, years) in count.items()]        
    return sorted( count, key=lambda x: x[1], reverse=True )


def display_statistics( monitor_data, categories ):
    '''Counts the number of different values for specific monitors.'''
    
    for category in categories:

        if category in FIELDS_TO_IGNORE:
            # Different value per (almost) every monitor
            continue
        
        values = _count_values( monitor_data, category )   
        if len(values) == 1:
            # Same value for all monitors
            val, _, _, _ = values[0]
            print(f'# Atrybut "{category}": ta sama wartość ("{val}") '
                  'dla wszystkich plików.\n')
            continue

        attr_title = category.title()
        print( f'\n# Atrybut "{attr_title}":\n')
        if attr_title == 'Title':
            print('(znak @ oznacza dowolną liczbę)\n')
            
        for value, number, min_year, max_year in values:
            if min_year == 0 or max_year == 0:
                print( f'"{value}": {number}')
                continue

            if min_year == max_year: time_info = f'w roku {min_year}'
            else: time_info = f'lata {min_year}-{max_year}'          
            print( f'"{value}": {number} ({time_info})' )

        print('\n')


def get_and_show_statistics():

    if FOLDER:
        folder = Path(FOLDER).absolute()
    else:
        folder = Path().absolute()
        if folder.name.endswith('system32'): #Windows double-click launcher
            folder = Path( __file__ ).parent.absolute() #Use script dir

    if not folder.exists():
        error('Nie znaleziono folderu "{folder}". Upewnij się, że podajesz '
              'dobrą ścieżkę')
        return

    print(f'### Aktywny folder: {folder}')
    monitors = [p for p in folder.iterdir() if p.suffix=='.pdf']
    if not monitors:
        error(f'W folderze {folder} nie ma żadnych plików PDF')
        return
        
    data, categories = _get_metadata_from_pdfs( monitors )
    display_statistics( data, categories )
    return data


if __name__ == '__main__':

    # UWAGA: gdyby po naszych zmianach wyskakiwał błąd SyntaxError,
    # to znaczy że coś popsuliśmy swoimi zmianami. W takim wypadku
    # najlepiej pobrać skrypt od nowa.

    # W tym miejscu można zmienić True na False, jeśli chcemy używać skryptu
    # na innych plikach PDF niż egzemplarze Monitora

    USE_ON_MONITORS_ONLY = True

    # W tym miejscu możemy wpisać między cudzysłowami ścieżkę
    # do własnego folderu z Monitorami
    
    FOLDER = ""

    # Tutaj można wpisać (w cudzysłowach i oddzielone przecinkami) nazwy pól,
    # Których nie chcemy liczyć do statystyk

    FIELDS_TO_IGNORE = ("Jakieś pole", "Jakieś inne pole")

    # Można wybrać, czy chcemy korzystać z wielu rdzeni komputera.
    # Przetwarzanie powinno być kilka razy szybsze, ale w razie gdyby
    # coś nie działało, można to wyłączyć 
    
    USE_MULTIPROCESSING = True

    # Jeśli chcemy po odczytaniu danych jeszcze je analizować, zmieniamy
    # tutaj na True (domyślnie: False)

    ANALYZE_INTERACTIVELY = False

    # !!
    # A rzeczy poniżej nie ruszamy!
    # Don't change the things below!

    if USE_ON_MONITORS_ONLY:
        FIELDS_TO_IGNORE = ('File size', 'Pages', 'ModDate', 'CreationDate')
              
    if PDFINFO_PATH:
        metadata = get_and_show_statistics()

    if not RUNS_IN_IDLE:
        if ANALYZE_INTERACTIVELY:
            interact( local=globals() )
        else:
            _ = input('\n[Naciśnij Enter, żeby zakończyć] ')
