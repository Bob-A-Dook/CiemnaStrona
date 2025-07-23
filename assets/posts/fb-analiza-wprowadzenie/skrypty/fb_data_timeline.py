'''
This module contains some general functions for analyzing JSON data
downloaded from Facebook, getting timestamped events from multiple
files and mixing them to get a sort of a timeline.

JSON encoding problem solved thanks to:
https://stackoverflow.com/questions/50008296/facebook-json-badly-encoded
'''
__author__ = 'Bob-A-Dook'
__email__ = "bob.adook@tutanota.com"
__license__ = 'MIT'

########################################
# Imported standard modules and globals
########################################

from json import load as json_load
from datetime import datetime
from pathlib import Path
from logging import error
from pprint import pprint
from zipfile import ZipFile

OUT_FILE = 'fb_moja_os_czasu.txt'

NAME_TO_LABEL = {
    'your_search_history.json': 'WYSZUKANE',
    "advertisers_you've_interacted_with.json": "REKLAMA",
    'viewed.json': 'OBEJRZANE NA TABLICY',
    'visited.json': 'ODWIEDZONA STRONA/PROFIL',
    'preferences.json': 'ZMIANA PREFERENCJI',
    'logins_and_logouts.json': 'LOGOWANIE',
    'account_activity.json': 'AKTYWNOŚĆ URZĄDZENIA'
    }

# Variables controlling FB event display
SPACING = '   '
FIRST_ROW_SPACING = '  '
LINE_SPACING = '\n'

########################################
# Helper functions
########################################

def _fix_fb_text_encoding(text):
    return text.encode('latin_1').decode('utf-8')


def _convert_timestamp( timestamp ):
    return datetime.fromtimestamp( timestamp )


def _format_time( timestamp ):
    return timestamp.strftime( '%Y-%m-%d %H:%M:%S' )


def fb_print( text ):
    '''Handles displaying emoji in programs which don't support them'''
    try:
        print(text)
    except UnicodeEncodeError:
        print(bytes(str(text), 'utf-8'))


def _clean_data(item):
    '''Fixes encoding or timestamp, depending on the provided data'''
    try:
        name, value = item     
        if isinstance(value, str):
            value = _fix_fb_text_encoding( value )
        elif name == 'timestamp' and isinstance(value, int):
            value = _convert_timestamp( value )
    except Exception:
        return item

    return (name, value)


def _get_facebook_info_folder():
    '''
    Automatically locates the folder with Facebook data in the current
    directory.
    '''
    all_files = [f for f in Path().iterdir()]
    subfolders = [f for f in all_files if f.is_dir()]
    if subfolders:
        folder = Path()
    else:
        try:
            zip_folder = [f for f in all_files if f.suffix == '.zip'][0]
            print('UWAGA: Dane ładowane prosto z pliku zip')
            folder = ZipFile( zip_folder )
        except IndexError:
            error('Nie znaleziono pliku zip ani folderów z danymi')
            folder = None

    return folder


def _get_json_files( folder, files_to_get=None, files_to_skip=None ):
    '''Recursively gets paths to all JSON files nested in a folder.'''  
    
    if not files_to_skip: files_to_skip = []

    if isinstance(files_to_skip, str): files_to_skip = [files_to_skip]
    if isinstance(files_to_get, str): files_to_get = [files_to_get]

    is_valid = lambda path: all([path.suffix == '.json',
                                     path.name not in files_to_skip])

    if isinstance(folder, ZipFile):
        files = [Path(f) for f in folder.namelist()]
    else:
        files = [path for path in Path(folder).rglob('*')]

    files = [(path.name, path) for path in files if is_valid(path)]                   
    if files_to_get:
        files = [(n, p) for (n,p) in files if n in files_to_get]

    return files


def _load_json( file, folder):
    '''An abstraction for loading both standalone and zipped files'''
    if isinstance(folder, ZipFile):
        return json_load( folder.open( str(file.as_posix())) )
    else:
        with open(file) as datafile:
            return json_load(datafile)
    

def aggregate( attrs_per_file, filter_out=None, get_unique=False ):
    '''
    Aggregates the per-file results into a single list, optionally
    filtering some of them out or getting only the unique ones.
    '''

    if filter_out:
        aggregated = [n for v in attrs_per_file.values() for n in v
                      if not filter_out(n)]
    else:
        aggregated = [n for v in attrs_per_file.values() for n in v]        

    if get_unique:
        aggregated = sorted(list(set( aggregated )))

    return aggregated

##################################################
# General functions and classes for analyzing data
##################################################

def recurse_into_data( data, data_analyzer, results, **options ):
    '''
    Recurses into the data from a single file, launching the
    data-analyzing function at each level or until the function
    returns `False`.
    All results are passed into the same list, `results`.
    '''
    
    keep_going = data_analyzer( data, results, **options )
    if keep_going == False:
        return
    
    if isinstance(data, dict):      
        for name, sub_data in data.items():
            if isinstance(sub_data, (list,dict)):
                recurse_into_data( sub_data, data_analyzer, results, **options )
                
    elif isinstance(data, list):
        for sub_data in data:
            recurse_into_data( sub_data, data_analyzer, results, **options )

    
def analyze_json_files( data_analyzer,
                        files_to_get=None, files_to_skip=None,
                        get_aggregate=True,
                        **options ):
    '''The general function for analyzing JSON data files from Facebok'''

    
    folder = _get_facebook_info_folder()
    if not folder: return []
    json_files = _get_json_files( folder, files_to_get, files_to_skip )
    if not json_files: return []

    full_results = {}
    for name, path in json_files:
        
        data = _load_json( path, folder )
        
        results = []            
        recurse_into_data( data, data_analyzer, results,
                           file_info=name, **options )
        
        if results:
            res_for_file = results[:]
            full_results[ name ] = res_for_file

    if get_aggregate:
        full_results = aggregate( full_results )

    return full_results


class FbEvent:
    '''Represents a single action on Facebook with a timestamp'''

    def __init__(self, data):
        for name, value in data:
            if not value: self.tag = name
            else: setattr(self, name, value)

    def _to_string(self):
        '''Converts the event's timestamp and data to text.'''
        
        event_attrs = self.__dict__.copy()
        date = _format_time( event_attrs.pop('timestamp') )
        try: tag = event_attrs.pop('tag')
        except Exception: tag = ''

        event_parts = []
        first_row = date + FIRST_ROW_SPACING + tag
        event_parts.append( first_row )

        indent = len(date)*' ' + SPACING       
        other_rows = ['{}{}: {}'.format(indent, k,v)
                       for (k,v) in event_attrs.items()]
        event_parts += other_rows
        
        return '\n'.join(event_parts)

    def write_to_file(self, open_file):
        '''Writes the event in text form into a file object'''
        event_as_text = self._to_string()
        print( event_as_text, LINE_SPACING, file=open_file )
        
    def __str__(self):
        return self._to_string()


def save_events_to_file( fb_events ):
    '''Formats FB events as text and saves them a text file'''
    if not fb_events: return
    
    with open( OUT_FILE, 'w', encoding='utf-8') as out:
        for event in fb_events:
            event.write_to_file( out )          
    print('Zapisano zdarzenia z FB do pliku "{}"'.format(OUT_FILE))


def _sort_by_timestamp( fb_events ):
    return sorted( fb_events, key=lambda x: x.timestamp )
        
########################################
# Specific data analyzers
########################################

'''
All data-analyzing functions MUST accept a structure with data (normally dict)
and a list of results which they add items to.
They are called at each level of depth, as the main function is recursing
into data.
If you want to send a signal to stop recursing, use `return False`.
'''

def _get_descriptions( data, results, **options ):
    if isinstance(data, dict) and 'description' in data:
        results.append( _fix_fb_text_encoding( data['description'] ))


def _get_attribute_names( data, results, **options ):
    if isinstance(data, dict):
        res = [k for k in data.keys() if not k in results]
        results += res


def _get_off_facebook_activity( data, results, **options ):
    
    try: off_activity = data['off_facebook_activity']
    except KeyError:
        error('Nie udało się zapisać aktywności spoza Facebooka!')
        return

    for item in off_activity:
        try:
            name = ('name', item['name'])
            basic_info = [(n,v) for ev in item['events']
                          for (n,v) in ev.items()]                    
            basic_info.append(name)
            basic_info = [_clean_data(item) for item in basic_info]
            basic_info.insert(0, ('AKTYWNOŚĆ POZA FB', ''))
            results.append( FbEvent( basic_info ) )
        except Exception as e:
            continue


def _get_names( data, results, **options ):
    if 'name' in data and not 'description' in data:
        fixed_name = _fix_fb_text_encoding( data['name'] )
        results.append( fixed_name )


def _get_search_results( data, results, **options ):

    try: searches = data['searches']
    except KeyError:
        error('Nie udało się zapisać wyników wyszukiwania')
        return
    
    for item in data['searches']:
        try:
            text = item['data'][0]['text']
            basic_info = [('timestamp', item['timestamp']),
                          ('text', text)]

            file_info = 'your_search_history.json'
            try: basic_info.insert( 0, (NAME_TO_LABEL[file_info], '') )
            except KeyError: pass

            basic_info = [_clean_data(item) for item in basic_info]
            results.append( FbEvent( basic_info) )
        
        except Exception:
            pass
            
            
def _get_events( data, results, file_info=None ):
    '''Gets timestamps with accompanying data and converts to FbEvents'''
    
    if not isinstance(data, dict): return

    basic_info = []

    # Special case for off-FB activity
    if 'off_facebook_activity' in data:
        _get_off_facebook_activity( data, results )
        return False

    # Special case for search history
    elif 'your_search_history.json' in file_info:
        _get_search_results( data, results )
        return False
         
    if not 'timestamp' in data: return # Not False, because you can go deeper

    # Special case for items with "data" fields
    try:
        data_item = data.pop('data')
        basic_info += [(name, value) for (name,value) in data_item.items()]
    except Exception as e:
        pass
            
    # General case for timestamped info
    basic_info += [(name, value) for (name,value) in data.items()]
           
    if len(basic_info) <= 1: return

    if file_info:
        try: basic_info.insert( 0, (NAME_TO_LABEL[file_info], '') )
        except KeyError: pass
        
    basic_info = [_clean_data(item) for item in basic_info]
    results.append( FbEvent( basic_info ) )

########################################
# Timeline creator and usage examples
########################################

if __name__ == '__main__':

    '''
    ## USAGE EXAMPLES:

    # Finding label names in all files
        
        attrs_per_file = analyze_json_files(_get_attribute_names,
                                            get_aggregate=False )  
        unique_attrs = aggregate( attrs_per_file,
                                  filter_out=lambda x: '*' in x,
                                  get_unique=True)
        pprint(unique_attrs)

    # Getting a list of visited pages (only 1 latest visit per page)

        visits = analyze_json_files( _get_names, files_to_get='visited.json')
        for v in visits: fb_print(v)

    # Getting only off-Facebook activities from our timeline

        off_fb = [ev for ev in timeline if ev.tag == 'AKTYWNOŚĆ POZA FB']
        for item in off_fb: print_fb(item)
    '''

### OŚ CZASU DLA NASZEJ AKTYWNOŚCI

    to_skip = ['notifications.json', 'used_ip_addresses.json', 'viewed.json']
    #to_skip = [] # Usuń pierwszy znak "#" z linijki, jeśli chcesz wszystko

    all_events = analyze_json_files( _get_events, files_to_skip=to_skip)
    timeline = _sort_by_timestamp( all_events )
    save_events_to_file( timeline )
