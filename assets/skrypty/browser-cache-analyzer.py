'''
! This is the Polish version of the script; only this note
and the code are in English.

This is a script for extracting entries from your computer's browser
cache for the purpose of analysis (e.g. to check what files
it stores, from which URLs they came etc.).
It works for Chromium-based browsers and Firefox, but it may change if they
ever modify the format of cache entries.

Code for parsing Chromium cache entries comes from ChromiumCacheExplorer
by kakkoko (https://github.com/kakkoko/ChromiumCacheExplorer/).

Code for parsing Firefox cache entries comes from FirefoxCache2
by singleye (https://github.com/singleye/FirefoxCache2).
'''
__author__ = 'Bob Adook'
__mail__ = 'bob.adook@tutanota.com'


from pathlib import Path
from re import search as re_search
from logging import warning, error
from typing import Union
from urllib.parse import urlparse
from time import time as get_time
from struct import unpack
from binascii import crc32 as binascii_crc32
from hashlib import sha256 as hashlib_sha256
from sys import flags, modules # To check for interactive mode
from platform import system
sysname = system()

#################################################
# Checking if the script runs in interactive mode
#################################################

def _check_if_interactive():
    '''
    Checks how the script was launched; it should behave differently
    if launched in a non-interactive way.
    '''
    runs_in_idle = 'idlelib' in modules
    got_interactive_flag = flags.interactive
    is_interactive = any((runs_in_idle, got_interactive_flag))
    return is_interactive

INTERACTIVE_MODE = _check_if_interactive()

##################################
# Some program strings and globals
##################################

DEBUG_MODE = False

MAX_FILENAME_LENGTH = 100
DEFAULT_OUTPUT_FOLDER = 'Extracted_from_cache'
IMAGE_FORMATS = ('.png','.jpg','.jpeg','.svg', '.gif', '.webp')

SCRIPT_PATH_INFO = ('Aby podać własną ścieżkę, edytuj zmienną CUSTOM_PATH na '
                    f'końcu tego skryptu ({Path(__file__).absolute()})')

CACHE_PATHS_WARN = ('Skrypt nie zna domyślnych ścieżek do pamięci podręcznych '
                    f'na Twoim systemie ({sysname}).\n{SCRIPT_PATH_INFO}')
                                        
###################################################
# Paths for various system and browser combinations
###################################################

ALIASES = {'Darwin': 'MacOS'}
if sysname in ALIASES:
    sysname = ALIASES[ sysname ]

if sysname == 'MacOS':
    warning('Nie testowałem skryptu na MacOS, ścieżki do pamięci podręcznej '
            f'mogą nie być prawidłowe.\n{SCRIPT_PATH_INFO}')
            
    
DEFAULT_CACHE_LOCATIONS = {
    
    'Linux': {
        'Firefox': '~/.cache/mozilla/firefox/*.default/cache2/entries',
        'Chromium': '~/.cache/chromium/Default/Cache',
        'Opera': '~/.cache/opera/Cache',
        'Vivaldi': '~/.cache/vivaldi/Default/Cache'
        'Brave': ('~/.cache/BraveSoftware/Brave-Browser/Default/Cache'
                  '/Cache_Data')
        },
    
    'Windows':{
        'Firefox': (r'~/AppData\Local\Mozilla\Firefox\Profiles\*.default'
                    r'\cache2\entries'),
        'Chrome': r'~/AppData\Local\Google\Chrome\User Data\Default\Cache'
        
        #'Edge': r'~/AppData\Local\Microsoft\Edge\User Data\Default\Cache',
        # Edge is currently not working, its cache format seems different      
        },

    'MacOS': {
        'Chrome': (r'~/Library/Application Support/Google/Chrome/Default/'
                   r'Application Cache')
        }
    }


caches = []
try: caches = DEFAULT_CACHE_LOCATIONS[ sysname ]
except KeyError: warning( CACHE_PATHS_WARN )
else:
    print(f'System: {sysname}. Skrypt zna domyślne ścieżki do '
          f'pamięci przeglądarek: {", ".join(name for name in caches)}. '
          'Zaraz poszuka w nich plików.\n')
    
CACHES_ON_THIS_COMPUTER = caches

##################
# Helper functions
##################

def __get_real_cache_paths( text_path ):
    '''
    Converts path in readable text form (with wildcards) into actual
    paths available on the computer.
    '''
    paths = []
    if text_path.startswith('~/'):
        paths = [p for p in Path.home().glob( text_path[2:])]
    return paths


class FileDuplicateError(Exception): pass

def _extract( data, url, folder ):
    '''
    A general function for extracting cache entries by converting their
    URL to file name and getting only the binary data.
    '''
    filename = urlparse(url).path.split('/')[-1]
    if len(filename) > MAX_FILENAME_LENGTH:
        filename = filename[-MAX_FILENAME_LENGTH:]
    folder = Path(folder)
    if not folder.exists(): folder.mkdir()
    out_path = folder / filename
    if out_path.exists():
        raise FileDuplicateError

    with open( out_path, 'wb') as out:
        out.write( data )
        
        
####################################
# Chrome and Chromium-based browsers
####################################

_FLAG_HAS_CRC32 = 0x01
_FLAG_HAS_KEY_SHA256 = 0x02

class ChromeCacheEntry:
    '''A single cache entry for Chromium-based browsers'''
    
    def __init__(self, file: Union[str, Path], browser:str) -> None:
        cache_file = Path(file)
        self.browser = browser
        
        with cache_file.open('rb') as src:
            data = memoryview(src.read())

        magic_number, version, key_length, key_hash, padding = unpack(
            '=QLLLL', data[:24])
        data = data[24:]
        if magic_number != 0xfcfb6d1ba7725c30:
            pass
            #raise ValueError('magic number mismatch')

        key = data[:key_length]
        data = data[key_length:]

        magic_number, flags, crc32, stream_size, padding = unpack(
            '=QLLLL', data[-24:])
        data = data[:-24]
        if magic_number != 0xf4fa6f45970d41d8:
            pass
            #raise ValueError('magic number mismatch')

        sha256 = None
        if flags & _FLAG_HAS_KEY_SHA256:
            data, sha256 = data[:-32], data[-32:]

        if len(data) != stream_size:
            data = data[:-stream_size]

            magic_number, flags, crc32, stream_size, padding = unpack(
                '=QLLLL', data[-24:])
            data = data[:-24]
            if magic_number != 0xf4fa6f45970d41d8:
                pass
                #raise ValueError('magic number mismatch')

            sha256 = None
            if flags & _FLAG_HAS_KEY_SHA256:
                data, sha256 = data[:-32], data[-32:]

            if len(data) != stream_size:
                raise ValueError('invalid stream size')

        if flags & _FLAG_HAS_CRC32 and binascii_crc32(data) != crc32:
            raise ValueError('crc32 mismatch')
        if sha256 and hashlib_sha256(data).digest() != sha256:
            raise ValueError('sha256 mismatch')

        self.file = cache_file
        url = key.tobytes().decode()
        self.url = url.split(' ')[-1] #Contains 3 URLs for some reason
        self.data = data

    def extract_data(self, folder):
        _extract( self.data, self.url, folder )

    def __repr__(self):
        return '<{} | {}>'.format( self.browser, self.url )

#########
# Firefox
#########

class FirefoxCacheEntry:
    '''
    A single Firefox cache entry, containing the data (such as the
    image inside) along with its URL.
    ''' 
    def __init__(self, filepath, browser):
        self.raw_data = None
        self.browser = 'Firefox'
        
        with open(filepath, 'rb') as fd:
            self.raw_data = fd.read()

        self.name = filepath.name

        self.data = None
        self.size = 0

        # metadata
        self.version = None
        self.fetch_count = 0
        self.last_fetch = None
        self.frequency = 0
        self.expire = None
        self.key = None
        self.key_len = 0
        self.url = ''
        self.entry_name = ''

        self._parse_metadata()

    def _parse_metadata(self):
        self.size = unpack('>I', self.raw_data[-4:])[0]
        self.data = self.raw_data[:self.size]
        chunk_size = 1024*256
        chunks = (self.size + chunk_size - 1)//chunk_size
        skip_bytes = 4 + chunks*2

        metadata_size = 32
        metadata_start = self.size + skip_bytes

        metadata = self.raw_data[metadata_start:metadata_start+metadata_size]

        self.version, \
        self.fetch_count, \
        self.last_fetch, \
        self.last_modify, \
        self.frequency, \
        self.expire, \
        self.key_len, \
        flags = unpack('>IIIIIIII', metadata)
        self.flags = flags if self.version >= 2 else 0

        metadata_block = metadata_start+metadata_size
        self.key = self.raw_data[metadata_block : metadata_block+self.key_len]
        self.url = self.key[1:].decode('utf-8').lstrip(',:')

    def __repr__(self):
        return '<{} | {} | {}>'.format(
            self.browser, self.last_fetch, self.url )
    
    def extract_data(self, folder):
        _extract( self.data, self.url, folder )

######################################
# Shared functions for extracting data
######################################

BROWSER_TO_CONTAINER = {
    'Firefox': FirefoxCacheEntry,
    'Chrome': ChromeCacheEntry,
    'Chromium': ChromeCacheEntry,
    'Opera': ChromeCacheEntry,
    'Vivaldi': ChromeCacheEntry,
    'Brave': ChromeCacheEntry
    #'Edge': ChromeCacheEntry # Currently not working!
    }

BROWSERS = list( BROWSER_TO_CONTAINER.keys() )


def __get_entries_for_browser( folder, browser, container ):
    '''Tries to get all cache entries for the specified browser'''
    
    files = [f for f in folder.iterdir()
             if f.is_file() and not f.name.endswith('index')]
    if not files:
        print(f'Nie znaleziono plików w pamięci przeglądarki "{browser}"')
        return []
    
    entries, errors = [], []
    for f in files:
        try: entries.append( container(f, browser) )
        except Exception as e:
            errors.append( (f, e) )

    if entries: print(f'Przeglądarka "{browser}": {len(files)} plików')
    if errors:
        if not entries: print(f'Przeglądarka "{browser}":')
        error(f'Błędy podczas odczytywania {len(errors)} plików')

    return entries


def get_cache_entries( cache_path=None, browser=None ) -> list:
    '''Gets all entries for all available browsers'''

    if cache_path:
        if browser:
            container = BROWSER_TO_CONTAINER[ browser ]
            return __get_entries_for_browser(
                Path(cache_path), browser, container )  
        error('Wskazano własny folder, ale bez nazwy przeglądarki! '
              'Wpisz przy zmiennej CUSTOM_BROWSER którąś z listy:\n'
              f'{", ".join(BROWSERS)}')
        return []

    if browser:
        if browser not in BROWSERS:
            error('Skrypt nie zna ścieżki do wpisanej przeglądarki '
                  f'({browser}). Być może literówka w nazwie?')
            return []
        
        cache_paths = [(b,path) for b,path in CACHES_ON_THIS_COMPUTER.items()
                       if b == browser]
    else:
        cache_paths = CACHES_ON_THIS_COMPUTER.items()
        
    getter_info = []
    for browser, cache_path in cache_paths:
        cache_folders = __get_real_cache_paths( cache_path )
        container = BROWSER_TO_CONTAINER[ browser ]
        for f in cache_folders: getter_info.append( (f, browser, container) )

    all_entries = []
    for folder, browser, container in getter_info:
        entries = __get_entries_for_browser( folder, browser, container )
        all_entries += entries

    return all_entries


def switch_to_interactive_mode( all_entries ):
    '''
    The script is designed for interactive work. If it is launched via the
    command line, it provides a restricted list of options.
    '''
    if not all_entries and not INTERACTIVE_MODE:
        warning('Skrypt nie znalazł żadnych plików w pamięciach podręcznych. '
                'Naciśnij dowolny klawisz, żeby go zamknąć')
        inp = input()
        return
 
    # Else no need to do anything, leave it to the launched REPL
    sep = '*' * 10
    MSG = ('\n[TRYB INTERAKTYWNY]\n\nSkrypt znalazł pliki w pamięciach '
           'podręcznych. Jeśli chcesz je analizować, są w zmiennej "entries".'
           '\nMożesz też korzystać z funkcji pomocniczych:\n'
           'get_entries, get_images, show_entries, extract_data.\n\n'
           'Aby po prostu skopiować pliki do osobnego folderu, wpisz '
           'któryś z tekstów oddzielonych kreską i naciśnij Enter:\n\n'
           'extract_all() | extract_images()\n')

    MSG = f'\n{sep}{MSG}{sep}\n'

    if INTERACTIVE_MODE:
        print( MSG )
        return

    def _to_interactive():
        # Solution from:
        # https://code-maven.com/switch-to-interactive-mode-from-python-script
        print(MSG)
        from code import interact
        interact( local=globals() )

    # Otherwise, show a list of options
    print('\n[UWAGA] Skrypt został wywołany przez konsolę. Jest lepiej '
          'przystosowany do pracy w trybie interaktywnym\n'
          '(czyli np. po uruchomieniu w IDLE albo wywołaniu przez wpisanie\n'
          f'`python -i {__file__}`)\n\n'
          'Twoje opcje (wpisz liczbę i potwierdź Enterem):\n')

    options = {
        1: ('Kopiuj wszystko do osobnego folderu', extract_all),
        2: ('Kopiuj same obrazki do osobnego folderu', extract_images),
        3: ('Przejdź do trybu interaktywnego', _to_interactive)
        }

    options_enum = [op for op in options.items()]
    for i, (description, opt) in options_enum:
        print(f'[{i}] {description}')

    answer = input('\nTWÓJ WYBÓR: ')
    try:
        chosen_action = options[ int(answer) ][-1]
        chosen_action()
    except Exception:
        error('Nieznana opcja. Możesz wybrać następujące: '
              f'{", ".join(options_enum)}')
        _ = input('Naciśnij Enter, żeby zakończyć')
    

#################################################
# Shorthand functions for analysis and extraction
#################################################

entries = [] # Do not move down, functions refer to it!

def get_entries( entrylist=None, extensions=None, browser=None,
                 url_text=None, regex=False ):
    '''
    The general function for getting data from the listed cache entry files.
    You can give it specific parameters to only select some files.
    '''
    if entrylist: results = entrylist
    else: results = entries[:]

    if type(extensions) == str: extensions = [extensions.lower()] 
    if extensions: results = [e for ext in extensions for e in results
                              if urlparse(e.url).path.lower().endswith(ext) ] 
    if browser:
        if type(browser) == list:
            results = [e for e in results if e.browser in browser]
        else: results = [e for e in results if e.browser == browser]
        
    if url_text:
        if regex: results = [e for e in results if re_search(url_text, e.url)]
        else: results = [e for e in results if (url_text in e.url)]
            
    return results


def show_entries( *args, **kwargs ):
    '''Displays a sorted list of all entries'''
    
    if len(args) == 1 and not 'entrylist' in kwargs: to_show = args[0]
    elif 'entrylist' in kwargs: to_show = kwargs[ 'entrylist' ]
    else: to_show = get_entries( **kwargs )

    def _get_domain(url):
        domain = ''.join( char for char in reversed(urlparse(url).netloc) )
        # Reversed to avoid e.g. cdn.website.pl > cookie.pl > website.pl
        return domain

    sorter_function = lambda e: (e.browser, _get_domain(e.url), e.url)
    to_show = sorted( to_show, key=sorter_function )
    for e in to_show: print(e)


def get_images( **kwargs ):
    '''A shorthand for getting the cache entries which contain images'''
    return get_entries( **kwargs, extensions=IMAGE_FORMATS )


def extract_data( *args, entrylist=None, images_only=False, folder=None,
                  **kwargs ):
    '''Copies files from inside the cache objects to a separate folder'''

    if not entrylist:
        if not args:
            entrylist = get_entries( **kwargs )
        elif len(args) == 1:
            entrylist = args[0]
        
    if images_only:
        extractable = get_images( entrylist=entrylist, **kwargs )
        f_tag = 'obrazki'
    else:
        extractable, f_tag = entrylist, 'pliki'
    
    # Prompt user if the number of files is large 
    if len(extractable) > 1000:
        print(f'\n[UWAGA] Znalezione {f_tag} ({len(extractable)}) po '
              'skopiowaniu mogą zająć sporo miejsca na dysku. Jeśli na pewno '
              'chcesz je skopiować, naciśnij Enter')
        inp = input('ENTER ')

    # Create output folder and extract the files
    if folder: out_folder = folder
    else: out_folder = f'{DEFAULT_OUTPUT_FOLDER}_{int(get_time())}'
    out_folder = Path(out_folder).absolute()
    if not out_folder.exists(): out_folder.mkdir()

    print('Kopiuję pliki...')
    duplicates, extracted, errors = 0, 0, 0
    for entry in extractable:
        try:
            entry.extract_data( out_folder )
            extracted += 1
        except FileDuplicateError:
            duplicates += 1
        except OSError: pass
        except Exception as e:
            errors += 1
            if DEBUG_MODE: error(f'Błąd podczas wyciągania pliku: {e}')

    if duplicates or errors:
        if duplicates:
            warning(f'Nie przeniesiono niektórych plików ({duplicates}), '
                    'bo pliki o takich samych nazwach już były w folderze')
        if errors:
            warning(f'Niektórych plików ({errors}) nie przeniesiono, bo '
                    'wystąpiły inne błędy')
        
    print(f'Skopiowano {f_tag} ({extracted}) do folderu:\n{out_folder}')


def extract_all():
    '''A less flexible, not filtering alias to `extract_data`'''
    extract_data()


def extract_images( *args, **kwargs ):
    '''Copies images from inside the cache objects to a separate folder'''
    extract_data( *args, **kwargs, images_only=True )


if __name__ == '__main__':

    # Przy CUSTOM_PATH możesz wkleić ścieżkę do folderu z pamięcią podręczną,
    # który chcesz sprawdzić (w takim wypadku musisz też podać nazwę
    # przeglądarki jako `CUSTOM_BROWSER`)

    CUSTOM_PATH = ""

    # Przy CUSTOM_BROWSER możesz wpisać nazwę przeglądarki
    # Jeśli tego nie zrobisz, to skrypt poszuka dla wszystkich, jakie zna.
    # Jeśli to przeglądarka oparta na silniku Chromium, to jest szansa,
    # że zadziała wpisanie "Chromium".
       
    CUSTOM_BROWSER = ""

    # A tych funkcji poniżej najlepiej nie zmieniać ;)
    entries = get_cache_entries( cache_path=CUSTOM_PATH,
                                 browser=CUSTOM_BROWSER )
    switch_to_interactive_mode( entries )

