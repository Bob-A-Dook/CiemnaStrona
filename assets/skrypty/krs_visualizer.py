'''
! This is the Polish version of this module. Only the code is in English. 

JEŚLI CHCECIE ZMIENIĆ DOMYŚLNE OPCJE, ZNAJDZIECIE JE NA KOŃCU SKRYPTU.

Skrypt odczytuje dane z plików PDF pobranych z KRS-u
(Krajowego Rejestru Sądowego) i przedstawia wydarzenia na osiach czasu.

INSTRUKCJA:

Na początek potrzebujecie plików PDF z KRS-u. Możecie znaleźć je tutaj:
https://ekrs.ms.gov.pl/web/wyszukiwarka-krs/strona-glowna/index.html

Zaznaczacie pola i wpisujecie nazwę firmy. Jeśli coś się pojawi,
to klikacie przy tej pozycji "Wyświetl", a następnie opcję "Pobierz wydruk
informacji PEŁNYCH" na dole. Pobierze wam się plik PDF.

Umieśćcie tego PDF-a w jakimś folderze (najlepiej tym samym, w którym jest
ten skrypt). Potem odpalcie skrypt (np. otwierając go w domyślnym edytorze
IDLE i naciskając klawisz F5).

Wyniki (wykresy w formacie JPG) pojawią się w podfolderze "Wykresy",
w tym samym miejscu co źródłowe PDF-y.

POTRZEBNE MODUŁY:

* Zewnętrzne moduły Pythona – BeautifulSoup, Matplotlib
* Zewnętrzne programy – `pdftohtml` (część biblioteki Popplera)
  do konwertowania plików PDF.
'''

__author__ = 'Bob Adook'
__mail__ = 'bob.adook@tutanota.com'
__license__ = 'MIT'

# ^ In short: just use it however you want ;) No strings attached.
# However, I take no responsibility for anything you do.

import re
import shutil
import logging
import tempfile
import datetime
import subprocess
from sys import platform
from pathlib import Path
from textwrap import wrap
from collections import Counter

try:
    from bs4 import BeautifulSoup    
except ImportError:
    BeautifulSoup = None
    logging.error('\nBrak biblioteki BeautifulSoup, bez niej nie odczytamy '
                  'danych! Aby ją zainstalować, wpisz w konsoli '
                  '"pip install beautifulsoup4", a potem '
                  '"pip install lxml"\n')
try:
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
except ImportError:
    plt, mdates = None, None
    if platform == 'win32': command = 'pip install matplotlib==3.3.1'
    else: command = 'pip install matplotlib'
    logging.error('\nBrak biblioteki Matplotlib, bez niej nie stworzymy '
                  'wykresów! Aby ją zainstalować, wpisz w konsoli '
                  f'"{command}"\n')

IMPORTS_SUCCESSFUL = all([BeautifulSoup, plt, mdates])

########################
# Checking for pdfothtml
########################

def _find_pdf_converter():
    '''
    Looks for a PDF converter (`pdftohtml`), either in PATH 
    or recursively in the current folder.
    '''
    converter = shutil.which('pdftohtml')
    if converter: return converter

    # If no program on PATH, search in the current folder
    files = [f.absolute() for f in Path().rglob('*')
             if 'pdftohtml' in f.name]
    if files:
        converter = str( files[0] )
    if converter: return converter

    # If no converter is found, show installation tips
    win_url = ('https://github.com/oschwartz10612/poppler-windows/'
               'releases/download/v21.10.0-0/Release-21.10.0-0.zip')
    mac_url = 'https://macappstore.org/poppler/'
    linux_url = ('https://stackoverflow.com/questions/'
                 '32156047/how-to-install-poppler-in-ubuntu-15-04')
                 
    logging.error(
        'Nie znaleziono programu `pdftohtml`. Aby go pobrać:\n\n'
        f'Na Windowsie pobierz zipa z adresu [{win_url}] i rozpakuj '
        'go w tym samym folderze co ten skrypt.\n\n'
        f'Na MacOS postępuj zgodnie z instrukcjami z [{mac_url}].\n\n'
        'Na Linuksie powinny zadziałać instrukcje z pierwszej odpowiedzi '
        f'([{linux_url}]).\n')

    if platform == 'win32':
        logging.error('Gdyby wyświetlał się komunikat o braku pliku '
                      '"MSVCP140.dll", to pobierz go z podanego adresu '
                      'i zainstaluj, klikając plik EXE:\n'
                      'https://aka.ms/vs/17/release/vc_redist.x64.exe\n')

    return None

CONVERTER = _find_pdf_converter()

##########################
# Matplotlib configuration
##########################

DEFAULT_WIDTH = 9
DEFAULT_HEIGHT = 20

TITLE_PARAMS = {'pad':12, 'fontsize':15, 'fontweight': 'bold'}
X_TICK_PARAMS = {'rotation':45, 'ha':'right'}
GRID_PARAMS = {'color':'white', 'linestyle':'dashed'}
SINGLE_BAR_PARAMS = {'edgecolor':"white", 'color':'#2c61da'}
MULTI_BAR_PARAMS = {'color':'#4ac8c7', 'edgecolor':'gray'}
BAR_TEXT_PARAMS = {'color':'white', 'ha':'center'}

SET_COMPANY_AS_TITLE = True
SHOW_START_DATES = True
SHOW_END_DATES = True

###########################
# Data getter configuration
###########################

# The format: "label: (regex to find section, regex to find subsection)"
AVAILABLE_GETTERS = {
    'nazwa':
    ('Dane podmiotu',
     '(Nazwa$|Firma, pod którą spółka działa)'),
    
    'wspólnicy':
    ('(Dane wspólników|Dane komplementariuszy|'
     'Osoby reprezentujące zagranicznego przedsiębiorcę w oddziale|'
     'Komitet założycielski)',
     'Nazwisko( / Nazwa lub firma)*'),
    
    'zarząd':
    ('Dane osób wchodzących w skład organu',
     'Nazwisko / Nazwa lub firma'),
    
    'adres':
    ('Siedziba i adres (podmiotu|oddziału)',
     'Adres( oddziału)*$')
    }

GRAPH_TITLES = { 'nazwa': 'Jak się zmieniały nazwy spółki',
                 'wspólnicy': 'Jak się zmieniali wspólnicy (udziałowcy)',
                 'zarząd': 'Osoby w zarządzie',
                 'adres': 'Adres firmy'}

# True: use single timeline, False: use waterfall plot
PLOT_TYPES = { 'nazwa': True, 'adres':True,
               'wspólnicy': False, 'zarząd':False}

DEFAULT_GETTERS = ('nazwa', 'wspólnicy')

# Adds first letters of graph types to output file names. Useful when
# you want multiple graphs in one folder without overwriting
USE_INFO_TAG = False

# If an entity (e.g. one of partners) changed their name, you can choose
# between displaying it as two separate ones or keeping the latest name
DISPLAY_LATEST_NAME_ONLY = False

##################################
# Functions for wrangling PDF data
##################################

def pdf_to_xml( pdf_file, converter ):
    '''Uses pdftohtml from Poppler utils to convert PDF to XML'''
    with tempfile.TemporaryDirectory() as tempdir:
        
        shutil.copy( pdf_file, tempdir )
                
        args = [converter, pdf_file.name, '-xml', '-i', '-nodrm', '-hidden']
        # -i for no images, -nodrm for anti-copy, -hidden for hidden text
        if platform == 'win32': sh_param = True # To hide flashing console
        else: sh_param = False
        p = subprocess.Popen(args, cwd=tempdir, shell=sh_param)
        p.wait()

        xml_path = Path(tempdir).joinpath(pdf_file.name).with_suffix('.xml')
        with open(xml_path, 'rb') as f: #'rb' needed for Windows!
            return BeautifulSoup( f, 'lxml' )
    

def _build_fontsize_map( xml ):
    '''Creates a fontID-to-size mapping'''
    font_elems = xml.find_all('fontspec')
    fmap = {elem.attrs['id'] : int(elem.attrs['size'])
            for elem in font_elems}
    return fmap
        

def get_textlines( xml: BeautifulSoup ):
    '''
    Parses PDF pages and recalculates the Y coordinates as if the PDF
    file was a single continuous page. Also converts XML object to
    custom TextLine objects. All this helps with getting text.
    '''
    pages = xml.find_all('page')
    font_sizes = _build_fontsize_map( xml )

    # Ignore empty segments or page number markers
    IGNORABLE_TEXT_RE = re.compile('(^Strona \d+ z \d+|^\s*$)')
    
    pdf_elems = []
    for i, page in enumerate(pages):

        page_center = int(page.attrs['width']) / 2
        page_height = int( page.attrs['height'])
        height_to_add = page_height * i
        
        for elem in page.find_all('text'):

            text = elem.text
            if IGNORABLE_TEXT_RE.match(text): continue
            
            left = int(elem.attrs['left'])
            right = left + int(elem.attrs['width'])
            
            top = int(elem.attrs['top'])
            top = top + height_to_add
            bottom = top + int(elem.attrs['height'])

            font = elem.attrs['font']
            fontsize = font_sizes[font]

            is_centered = left < page_center < right

            coords = left, right, top, bottom

            textline = TextLine( coords, text, fontsize, is_centered )
            pdf_elems.append( textline )

    return pdf_elems
            
            
class TextLine:
    '''An object corresponding to a line of text from a PDF'''

    __slots__ = ['left', 'right', 'top', 'bottom',
                 'text', 'fontsize', 'is_centered']

    def __init__(self, coords, text, fontsize, center):
        self.left, self.right, self.top, self.bottom = coords
        self.text = text
        self.fontsize = fontsize
        self.is_centered = center

    def __repr__(self):
        return f'<{self.top} {self.text}>'


def analyze_document_structure( itemlist ):
    '''
    Extracts the entry-to-date index and groups
    other data into sections.
    '''
    NO_INFO_TEXT = "Brak wpisów"
    HEADING_STARTERS_RE = re.compile('^(Rubryka|Podrubryka|Dział)')
    
    headers = [e for e in itemlist if e.is_centered and e.fontsize >= 13]
    # Header font size on Windows is different than on Linux! Avoid constants
    boundaries = {h: h.top for h in headers
                  if HEADING_STARTERS_RE.match(h.text)}

    if not boundaries:
        logging.error('W pliku nie znaleziono nagłówków zgodnych z tymi, '
                      'jakie mają pliki z KRS-u. Przetwarzanie niemożliwe.')
        return [],[]

    # Get text blocks from the starting entry-to-date index
    entry_dates = []
    for elem in itemlist:
        if elem in boundaries:
            break
        if elem.fontsize < 13:
            entry_dates.append( elem )

    # Get other document sections
    sections = {}
    nonsection_elems = []
    current_section = None
    for elem in itemlist:
        
        if elem in boundaries:
            # Reached heading; if not a skippable subheading,
            # start a new section
            if (current_section
                and current_section.endswith('Dane wspólników')
                and elem.text.startswith('Podrubryka')):
                #TODO: make it more elegant, perhaps a list of mismatching
                # heading + subheading combos
                continue
            
            current_section = elem.text
            nonsection_elems = []
            
        elif (current_section and elem.is_centered and elem.fontsize == 13):
            # Merge; but only if there are no smaller elements between
            # the heading and this text (supposedly its continuation)
                
            if elem.text == NO_INFO_TEXT: continue    
            if not nonsection_elems:
                current_section += f' {elem.text}'
                
        else:
            # Plain text, add to current section
            if current_section:
                try: sections[current_section].append(elem)
                except KeyError: sections[current_section] = [elem]
                nonsection_elems.append( elem )

    # Clear empty sections
    for section, entries in sections.items():
        if all(e.text == NO_INFO_TEXT for e in entries):
            entries.clear()
 
    sections = [Section(name, data) for (name, data) in sections.items()]
    return sections, entry_dates


def _get_end_date( itemlist, entry_map ):
    '''
    Searches the document for the date of lookup, which is used as
    fallback for last date if the company hasn't been crossed out.
    '''
    END_DATE_RE = re.compile('Stan na dzień (\d\d\.\d\d.\d\d\d\d)')
    end_date = None
    for elem in itemlist:
        if END_DATE_RE.match( elem.text ):          
            end_date = END_DATE_RE.search(elem.text).group(1)

    return end_date


def _get_section_header( section_items ):
    '''
    Gets information from the first row in order to create a mapping between
    x position and column name.
    '''
    # Create initial header
    by_y = sorted(section_items, key=lambda e: e.top)

    is_empty = lambda x: re.search('^ +$', x) is not None

    FIELD_TO_SPLIT = 'Nr wpisu'
    FIELD_TO_IGNORE = 'wprow. wykr.'
    
    first_item = by_y[0]
    header = {}

    # All headers have one field which needs to be split; find it first
    split_item_range = None
    for item in section_items:    
        if item.text == FIELD_TO_SPLIT:
            split_item_range = (item.left, item.right)
            break
    
    for item in section_items:
        x_coord = item.left
        if x_coord == first_item.left and not (item is first_item):
            #Got to next item; not a header anymore
            break
        elif (item.text == FIELD_TO_IGNORE
              or item.fontsize == 13 and item.is_centered
              or is_empty(item.text)):
            continue
       
        try:
            text = header[ x_coord ]
            header[ x_coord ] = text + ' {}'.format(item.text)
        except KeyError:
            header[ x_coord ] = item.text

    # Now add entries to the original header
    # (e.g. because some of the original ones should be split in two)
    unique_x_pos = sorted(list(set(item.left for item in section_items)))
    is_close_to = lambda x, val: x <= val <= x+2

    full_header = {}
    for item in section_items:

        x_pos = item.left
        try:
            full_header[ x_pos ] = header[ x_pos ]
        except KeyError:
            if not split_item_range: continue
            if is_close_to( x_pos, split_item_range[-1] ):
                full_header[ x_pos ] = header[ split_item_range[0] ] + ' (END)'
            else:
                full_header[ x_pos ] = 'UNKNOWN'
        
    return full_header


def _parse_section_data( section_name, section_items ):
    '''Detects main anchor points for the section: header and 1st column'''
    
    if not section_items: return {}, []
    
    section_header = _get_section_header( section_items )
    header_names = set(section_header.values())

    if not section_header:
        #TODO: Maybe catch such situations earlier? A section with no header
        # probably had only items without text
        return {}, []
    
    first_x_coord = min(k for (k,v) in section_header.items()
                        if section_header[k] != 'UNKNOWN')

    first_column_items = [it for it in section_items
                          if it.left == first_x_coord
                          and not it.text in header_names]
    #TODO: Decide on the basis of coords, not text
        
    if not first_column_items:
        column = []
    else:
        column = _merge_column_entries( first_column_items )

    return section_header, column


class Section:
    '''
    A self-contained part of the KRS dump. Usually contains a standard
    header and its first column contains either a sequence of numbers or
    categories.
    '''
    __slots__ = ['name', 'header', 'content',
                 'first_col', 'first_col_is_numeric']

    def __init__( self, name, items ):
        self.name = name
        self.content = items
        self.header, self.first_col = _parse_section_data( name, items )

        self.first_col_is_numeric = all(e.text.isnumeric()
                                        for e in self.first_col)

    def __repr__(self):
        sep = '\n -> '
        subcats = sep.join(c.text for c in self.first_col)
        return f'{self.name} ||{sep}{subcats}\n'        


def _merge_column_entries( column ):
    '''
    Merges lines if they appear to be divided (e.g. starts with number,
    then some lines without, then another line with number).
    Usually used for the 1st column; other ones are merged after the entries
    are classified.
    '''
    def _merge_lines( buffer, merged ):
        if buffer:
            if len(buffer) == 1:
                merged.append(buffer[0])
            else:
                # Modify only the first entry from the buffer
                total_bottom = buffer[-1].bottom
                merged_text = ' '.join(b.text for b in buffer)
                left = min(b.left for b in buffer)
                right = max(b.right for b in buffer)
                
                first_item = buffer[0]
                first_item.text = merged_text
                first_item.bottom = total_bottom
                first_item.left = left
                first_item.right = right
                
                merged.append( first_item )
                buffer = []
        return

    merged = []
    buffer = []    
    for it in column:
        if re.match( '\d+', it.text ):
            _merge_lines( buffer, merged )
            buffer = [ it ]
        else:
            buffer.append( it )

    _merge_lines( buffer, merged )
    return merged

##########################################
# Functions for getting data from sections
##########################################


def get_section_data( text, sections ):
    '''Gets section which contains a specific string of text'''

    text_re = re.compile( text )
    matching_section = [section for section in sections
                        if text_re.search( section.name )]

    if not matching_section:
        # Search first column names as well
        for section in sections:
            for field in section.first_col:
                if text_re.search( field.text ):
                    return section                
        return None
    
    if len(matching_section) > 1:
        logging.warning(
            f'Znaleziono więcej niż jedną sekcję z tekstem "{text}"')

    return matching_section[0]


def map_entries_to_dates( events ):
    '''Creates a mapping between KRS entries and their dates'''
    temp_map = {}
    for ev in events:
        try: temp_map[ ev.top ].append(ev)
        except KeyError: temp_map[ ev.top ] = [ev]

    temp_map = [(y,evs) for (y,evs) in temp_map.items() if len(evs) == 4]

    event_map = {}
    for _, events in temp_map:
        events.sort( key = lambda ev: ev.left )
        _, num, _, date = events
        event_map[ num.text ] = date.text
        
    return event_map
    
        
def _date_to_timestamp( date_string ):
    '''Converts the date (in Polish format) to datetime's timestamp'''
    if date_string in ('teraz','-'):
        return datetime.datetime.now().timestamp()
    ts = datetime.datetime.strptime(date_string, "%d.%m.%Y").timestamp()
    return ts


def _get_data_from_section( section, event_map ):
    '''
    Uses information from sections and the main event map to assign
    dates to particular events in the company's history.
    '''
    rev_header = {v:k for (k,v) in section.header.items()}
    
    start_date_pos = rev_header['Nr wpisu']
    end_date_pos = rev_header['Nr wpisu (END)']
    field_name_pos = rev_header['Numer i nazwa pola']
    field_value_pos = rev_header['Zawartość']
    
    # Get items to the left of first column and group them by y coords
    col_right_edge = section.first_col[0].right
    items_to_left = [elem for elem in section.content
                     if elem.left > col_right_edge]

    items_by_y = {}
    for it in items_to_left:
        y_pos = it.top
        try: items_by_y[ y_pos ].append( it )
        except KeyError: items_by_y[ y_pos ] = [ it ]

    categories = {}
    if not section.first_col_is_numeric:
        categories = {e.top : e.text for e in section.first_col}

    # Match events to their dates
    all_events = []
    prev_category = None
    for y_pos, line in items_by_y.items():
        event_info = {}

        # If no explicit category is given,
        # look for one in the first column
        if not section.first_col_is_numeric:
            try:
                category = categories[y_pos]
                event_info['category'] = category
                prev_category = category
            except KeyError:
                if prev_category:
                    event_info['category'] = prev_category
                    
        for it in line:
            x_pos = it.left
            text = it.text.strip()

            # Get start and end dates
            if x_pos == start_date_pos:
                try:
                    datestring = event_map[ text ]
                    event_info['start'] = datestring
                except KeyError:
                    if text == '-': event_info['start'] = text
                    elif text == 'wprow. wykr.':
                        pass # TODO: Make more elegant               
                
            elif x_pos == end_date_pos:
                if text == '-': datestring = text
                else: datestring = event_map[ text ]
                event_info['end'] = datestring

            # Get field names and values
            elif x_pos == field_name_pos:
                event_info['category'] = text

            elif x_pos == field_value_pos:
                event_info['value'] = text

        all_events.append( event_info )

    all_events = _merge_multiline_text( all_events )
    return all_events
    

def _merge_multiline_text( all_events ):
    '''Merges lines of text (not from first columns) into blocks.'''

    HEADER_VALUES = ('Numer i nazwa pola', 'Zawartość', 'L.p')
    full_event_len = max(len(ev) for ev in all_events)
    
    prev_full_event = None
    current_index = 1
    merged_events = []
    for event in all_events:

        if all( k in HEADER_VALUES for k in event.values() ):
            continue

        ind = None
        if all( (len(event) == 1, 'category' in event) ):
            try: ind = int( event['category'] )
            except Exception: pass
            if ind == current_index+1:
                #It's another entity
                current_index += 1
                #TODO: Maybe add to a separate group if a need arises

        if (not 'category' in event
            and all( [(v in event) for v in ('value','start','end') ])):
            # The same category as the one before it
            event['category'] = prev_full_event['category'] 
        
        if len(event) == full_event_len:
            merged_events.append( event )
            prev_full_event = event
            continue
        
        if (not 'start' in event and not 'end' in event):
            if 'category' in event:
                # It's still the same category, just divided into lines
                prev_full_event['category'] += f' {event["category"]}'
            if 'value' in event:
                prev_full_event['value'] += f' {event["value"]}'

    merged_events = _merge_first_and_last_names( merged_events )
    return merged_events


def _merge_first_and_last_names( events ):
    '''Merged first and last names while also handling their changes'''
    
    EMPTY_VALUE = '******'
    is_first_name = lambda e: e['category'].endswith('Imiona')
    is_last_name = lambda e: 'Nazwisko' in e['category']

    iter_events = (e for e in events)
    prev_event = next(iter_events)
    last_name_field = None
    cleaned = []  
    
    for event in iter_events:

        if not any(( is_first_name(event), is_last_name(event) )):
            cleaned.append( event )
            prev_event = event
            continue
            
        if is_first_name(event):      
            if is_last_name( prev_event ):
                last_name_field = prev_event

            first_name = event['value']
            last_name = last_name_field['value']
            if first_name == EMPTY_VALUE: first_name = ''
            merged_name = f'{first_name} {last_name}'.strip()
            
            if is_first_name( prev_event ):
                last_added_ev = cleaned[-1]
                print('[UWAGA] Zmiana imienia! Z '
                      f'{last_added_ev["value"]} na {merged_name}')
                last_added_ev['value'] = merged_name
            else:
                mod_event = event.copy()
                mod_event['value'] = merged_name
                for key in ('category','start','end'):
                    mod_event[key] = last_name_field[key]
                cleaned.append( mod_event )

        elif is_last_name(event) and is_last_name(prev_event):
            print('[UWAGA] Zmiana nazwy/nazwiska! Z '
                  f'{prev_event["value"]} na {event["value"]}') 
            if DISPLAY_LATEST_NAME_ONLY: pass
            else:
                cleaned.append( prev_event )
                #TODO: Handle changes of BOTH first and last names ;)
            
        prev_event = event
    return cleaned


class KrsEvent:
    '''An object corresponding to a single official change to a company'''

    def __init__(self, data_piece, end_date):

        start, end = data_piece['start'], data_piece['end']
        self.start_date = start
        self.start_ts = _date_to_timestamp(  start )
        
        if end == '-' and end_date:
            end = end_date
        self.end_date = end
        self.end_ts = _date_to_timestamp( end )
        self.name = data_piece['value']

    def __repr__(self):
        return f'< {self.name} | od {self.start_date} do {self.end_date} >'


def get_events( sections, date_map,
                data_getters=None, end_date=None ):
    '''
    Gets events (KrsEvent objects) related to the company's history.
    Uses the AVAILABLE_GETTERS mapping to convert user-friendly labels
    into the right regex for getting data from the sections.
    '''
    if not data_getters:
        data_getters = DEFAULT_GETTERS
        
    categories_to_get = []
    for label in data_getters:
        try:
            info = AVAILABLE_GETTERS[ label ]
        except KeyError:
            logging.error(f'Nieznana kategoria danych: {label}')
        else:
            categories_to_get.append( (label, info) )
        
    all_events = []
    for label, (main_category, subcat) in categories_to_get:

        title = GRAPH_TITLES[ label ]
        use_single_plot = PLOT_TYPES[ label ]
        
        section = get_section_data( main_category, sections )
        if not section:
            logging.error(f'Brak danych dla wykresu "{label}"')
            continue
        
        data = _get_data_from_section( section, date_map )
        data = [d for d in data
                if re.search( subcat.lower(), d['category'].lower() )]
        
        events = [KrsEvent(d, end_date) for d in data]
        if label == 'adres':
            for ev in events: ev.name = _shorten_address( ev.name )

        all_events.append( (use_single_plot, title, events ) )
        
    return all_events
  
##########################################
# Visualizing events on a Matplotlib graph
##########################################

def __shorten( text ):
    FULLNAME = 'SPÓŁKA Z OGRANICZON[AĄ] ODPOWIEDZIALNOŚCIĄ'
    return re.sub( FULLNAME, 'SP. Z O.O.', text )


def _shorten_address( address ):
    '''Removes less important info from the address text'''
    address = re.sub( ',\s+kod(.*?)poczta(.*?)kraj(.*?)$', '', address )
    return address.replace( 'miejsc. ','')


def _wrap_label( label, box_width=None ):
    '''Wraps label text to fit it to size'''

    label = __shorten( label )
    MIN_CHARS = 10
    MAX_CHARS = 30
    if box_width:
        LETTER_WIDTH = 16
        PADDING = 0
        letters_per_line = int((box_width - PADDING) / LETTER_WIDTH)
    else:
        letters_per_line = 20

    # Restrict size to available values
    letters_per_line = max(MIN_CHARS, min(MAX_CHARS, letters_per_line))
    return '\n'.join( wrap( label, letters_per_line ))


def _timestamp_as_date( ts ):
    date = datetime.datetime.fromtimestamp( ts )
    matplot_date = mdates.date2num(date)
    return date


def _format_date( d ):
    return f'{d.day}.{d.month:02}.{d.year}'


def _set_plot_colors():
    
    plt.rcParams['figure.facecolor'] = '#252525'
    plt.rcParams['text.color'] = '#ddd'
    plt.rcParams['axes.labelcolor'] = '#ddd'
    plt.rcParams['xtick.color'] = '#ddd'
    plt.rcParams['ytick.color'] = '#ddd'
    plt.rcParams['axes.facecolor'] = '#ddd' #Light background    


def _plot_single_bar( subplot, xticks, xlabels, names,
                      start_dates, end_dates, date_diffs ):                  
    '''
    Plots multiple events on a single bar. Used for non-overlapping
    events, such as company name or address changes.
    '''
    plt.yticks( [1] )
    
    subplot.barh(0,  date_diffs, left=start_dates, **SINGLE_BAR_PARAMS)
    subplot.margins( x=0, y=0 )

    subplot.xaxis.set_ticks( xlabels )
    subplot.set_xticklabels( xticks, **X_TICK_PARAMS )
    
    for i, (bar, name) in enumerate(zip( subplot.patches, names )):
        # Fit text into the center of the single horizontal bar
        width = bar.get_width()
        label = _wrap_label( name, box_width=width )
        x_pos = bar.get_x() + width / 2 # y is always 0 here
        subplot.text(x_pos, 0, label, va='center', **BAR_TEXT_PARAMS)
       

def _plot_multiple_bars( subplot, xticks, xlabels, names,
                         start_dates, end_dates, date_diffs ):                       
    '''
    Plots events as separate bars per each entity. Used for events which
    may overlap, such as adding and removing major shareholders.
    '''
    plt.yticks(range(len(names)), names)
    
    subplot.barh(range(len(start_dates)), date_diffs, left=start_dates,
                 **MULTI_BAR_PARAMS)
    subplot.margins( x=0 )
    subplot.set_axisbelow(True)
    subplot.grid( **GRID_PARAMS )
    
    subplot.xaxis.set_ticks( xlabels )
    subplot.set_xticklabels( xticks, **X_TICK_PARAMS )
    

def construct_graphs( raw_event_info, end_date, name ):
    '''Creates Matplotlib graphs for the data.'''

    event_info = []
    for use_single_bar, title, events in raw_event_info:
        event_info.append( (use_single_bar, title, events) )

    if not event_info:
        logging.warning('Nie udało się zebrać danych do stworzenia '
                        'jakiegokolwiek wykresu')
        return

    # Set general parameters
    _set_plot_colors()

    plot_num = len( event_info )
    bar_num_ratios = [1 if one_bar else len(events)
                      for one_bar,_, events in event_info]            
    fig, subplots = plt.subplots(
        plot_num, 1, gridspec_kw={'height_ratios': bar_num_ratios})

    if SET_COMPANY_AS_TITLE and name:
        plt.suptitle( name )

    # Then move to graph-specific stuff
    for i, (use_single_bar, title, events) in enumerate(event_info):
        
        data = [(_timestamp_as_date(ev.start_ts),
                 _timestamp_as_date(ev.end_ts),
                 ev.name)
                for ev in events]

        # Sort by start dates first, end dates second; earliest on top
        data.sort( key=lambda x: (x[0], x[1]), reverse=True )
        
        start_dates, end_dates, names = list(list(it) for it in zip(*data))
        date_diffs = [e - b for (e,b) in zip( end_dates, start_dates)]
        ylabels = [ _wrap_label(name, box_width=250) for name in names ]

        # Inform about repeating names
        # TODO: Verify if it's really the same person/company
        repeat_num = len(names) - len(list(set(names)))
        if repeat_num:
            print('[UWAGA] Niektóre nazwy/nazwiska pojawiają się na wykresie '
                  f'"{title}" wielokrotnie:')
            for name, num in Counter(names).items():
                if num > 1: print(f'{name}: {num} razy')
            print('\n')
                
        # Now modify the x-axis labels (dates of events)
        xlabels = []
        if SHOW_START_DATES: xlabels += start_dates
        if SHOW_END_DATES: xlabels += end_dates
        xlabels = list(set(xlabels))
        xticks = [_format_date(d) for d in xlabels]

        # Set plot title
        try: subplot = subplots[i]
        except TypeError: subplot = subplots
        plt.sca( subplot )
        subplot.set_title( title, **TITLE_PARAMS )

        # Finally, create a single- or multi-bar plot
        info = (subplot, xticks, xlabels, ylabels,
                start_dates, end_dates, date_diffs)

        if use_single_bar: _plot_single_bar( *info )
        else: _plot_multiple_bars( *info )
        
    return plt


def _make_info_tag( labels ):
    '''
    Creates a tag to be appended to the filename in order to show
    which graphs it contains.
    '''
    if not labels: return ''
    return ''.join(word[0] for word in labels)


def _get_company_name( sections, date_map ):
    '''Gets the latest name of the company'''
    evs = get_events( sections, date_map, data_getters=('nazwa',))
    name_evs = [e for _,_,e in evs][0]
    latest = sorted(name_evs, key=lambda ev: ev.end_ts)[-1]
    return latest.name


def _get_krs_id( singlepage ):
    '''Gets the KRS ID from the flattened document'''
    centered = (line for line in singlepage if line.is_centered)
    for textline in centered:
        krs_num = re.search('^Numer KRS: (\d+)\s*$', textline.text)
        if krs_num:
            return krs_num.group(1)


def _save_timeline( plt, pdf_path, info_tag, dimensions ):
    '''
    Scales plot to the final size and saves it to an image.
    The solution was adapted from a StackOverflow answer
    (https://stackoverflow.com/questions/32428193/
    saving-matplotlib-graphs-to-image-as-full-screen)
    '''    
    plt.subplots_adjust( wspace=0.4, hspace=0.4 )
    try:
        width, height = dimensions
    except Exception:
        width = DEFAULT_WIDTH
        height = DEFAULT_HEIGHT

    figure = plt.gcf()
    figure.set_size_inches( width, height )

    out_folder = pdf_path.absolute().parent / 'Wykresy'
    if not out_folder.exists(): out_folder.mkdir()
    out_name = out_folder.joinpath(pdf_path.name).with_suffix('.jpg')

    if info_tag:
        out_name = re.sub( '.jpg', f'_{info_tag}.jpg', str(out_name) ) 
    
    plt.savefig(out_name, bbox_inches='tight')
   
################
# Main functions
################
    

def create_krs_timeline( pdf_path, info_to_get=None, dimensions=None ):
    '''Creates a timeline for some pre-selected KRS events.'''

    if not IMPORTS_SUCCESSFUL or not CONVERTER: return 'NO_UTILS'

    converter = CONVERTER
    if isinstance(pdf_path, str):
        pdf_path = Path(pdf_path)

    try: xml = pdf_to_xml( pdf_path, converter )
    except Exception:
        logging.exception(
            f'Błąd podczas konwersji pliku {pdf_path.name}!')
        return
            
    text = get_textlines( xml )
    sections, entry_index = analyze_document_structure( text )
    if not sections or not entry_index:
        return 'INVALID_FORMAT'

    edate = _get_end_date( text, entry_index )
    date_map = map_entries_to_dates( entry_index )

    events = get_events( sections, date_map,
                         data_getters=info_to_get,
                         end_date=edate )

    try:
        krs_id = _get_krs_id( text )
        name = __shorten( _get_company_name( sections, date_map ) )
        if krs_id and name: name = f'KRS {krs_id}\n({name})'
    except Exception: name = ''

    plt = construct_graphs( events, edate, name )
    if not plt: return 'NO_GRAPHS'

    if USE_INFO_TAG: info_tag = _make_info_tag( info_to_get )
    else: info_tag = ''
    
    _save_timeline( plt, pdf_path, info_tag, dimensions )

    return 'SUCCESS'


def create_timelines_for_all( folder=None, **other_params ):
    '''The main function. Creates timelines for all PDFs from a folder'''

    if not IMPORTS_SUCCESSFUL or not CONVERTER: return
    
    if not folder or folder =='NAZWA': folder ='.'
    folder = Path(folder)
    if not folder.exists():
        logging.error(f'Nie znaleziono podfolderu "{folder.name}" w folderze '
                      f'{folder.absolute().parent}.\n'
                      'Musisz go najpierw stworzyć! :D')
        return
                      
    pdfs = [f for f in folder.iterdir() if f.suffix == '.pdf']
    if not pdfs:
        logging.error('Nie znaleziono żadnych plików PDF '
                      f'w folderze "{folder.absolute()}".')
        return

    print(f'Znaleziono pliki PDF ({len(pdfs)}) w folderze {folder.absolute()}')
    
    successes = 0
    for pdf in pdfs:
        print(f'\nPrzetwarzam {pdf}...\n')
        try:
            result = create_krs_timeline( pdf, **other_params)
            if result == 'NO_UTILS': break
            elif result == 'SUCCESS': successes += 1
        except Exception:
            logging.exception(f'Nie udało się stworzyć wykresów dla "{pdf}"')
            continue            

    if successes:
        print(f'\nStworzono wykresy dla {successes}/{len(pdfs)} plików PDF. '
              f'Trafiły do folderu:\n{folder.absolute()}')

    
if __name__ == '__main__':

    # W tym miejscu można zmieniać wymiary wykresu, jeśli jest nieczytelny
    # (w calach; domyślnie jest "width, height = 9, 20")
    
    width, height = 9,20

    # Tutaj można wpisywać, dla jakich kategorii mają powstać wykresy
    # (dostępne: 'nazwa', 'adres', 'zarząd', 'wspólnicy')
    
    info = ['nazwa','adres','zarząd','wspólnicy']

    # Między cudzysłowami możesz wpisać nazwę albo pełną ścieżkę folderu
    # Domyślnie: folder = "" (skrypt szuka w folderze, w którym go odpalamy)
    
    folder = ""

    # A tej funkcji poniżej nie ruszaj ;)  
    create_timelines_for_all( folder,
                              info_to_get=info,
                              dimensions=(width,height) )
