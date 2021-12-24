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
from platform import system
sysname = system()

##################################
# Some program strings and globals
##################################

MAX_FILENAME_LENGTH = 100
DEFAULT_OUTPUT_FOLDER = 'Extracted_from_cache'
IMAGE_FORMATS = ('.png','.jpg','.jpeg','.svg', '.gif', '.webp')

CACHE_PATHS_WARN = ('Skrypt nie zna domyślnych ścieżek do pamięci podręcznych '
                    f'na Twoim systemie ({sysname}). Będzie trzeba je '
                    'wpisać osobiście, jako CUSTOM_PATH, na końcu tego skryptu')
                    
###################################################
# Paths for various system and browser combinations
###################################################

DEFAULT_CACHE_LOCATIONS = {
    
    'Linux': {
        'Firefox': '~/.cache/mozilla/firefox/*.default/cache2/entries',
        'Chromium': '~/.cache/chromium/Default/Cache',
        'Opera': '~/.cache/opera/Cache',
        'Vivaldi': '~/.cache/vivaldi/Default/Cache'
        },
    
    'Windows':{
        'Firefox': (r'~/AppData\Local\Mozilla\Firefox\Profiles\*.default'
                    r'\cache2\entries'),
        'Edge': r'~/AppData\Local\Microsoft\Edge\User Data\Default\Cache',
        'Chrome': r'~/AppData\Local\Google\Chrome\User Data\Default\Cache'
        },
    }

BROWSERS = list(set( b_name for _, b_info in DEFAULT_CACHE_LOCATIONS.items()
                     for b_name in b_info ))

ALIASES = {'Darwin': 'MacOS'}

if sysname in ALIASES:
    sysname = ALIASES[ sysname ]

caches = []
try: caches = DEFAULT_CACHE_LOCATIONS[ sysname ]
except KeyError: warning( CACHE_PATHS_WARN )
else:
    print(f'System: {sysname}. Skrypt zna domyślne ścieżki do '
          f'pamięci przeglądarek: {", ".join(name for name in caches)}')
    
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
        warning(f'Plik o nazwie "{filename}" już jest w folderze "{folder}", '
                'skrypt nie będzie go nadpisywał')
        return
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
    'Edge': ChromeCacheEntry
    }

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
        error('Wskazano własny folder, ale bez nazwy '
                      'przeglądarki! Wpisz którąś z listy:\n'
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

#################################################
# Shorthand functions for analysis and extraction
#################################################

entries = [] #Should be here as a default

def get_entries( *args, extensions=None, browser=None,
                 url_text=None, regex=False ):
    
    if type(extensions) == str: extensions = [extensions.lower()]
    results = entries[:]
    
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
    if len(args) == 1 and not 'entrylist' in kwargs: to_show = args[0]
    elif 'entrylist' in kwargs: to_show = kwargs[ 'entrylist' ]
    else: to_show = get_entries( *args, **kwargs )

    def _get_domain(url):
        domain = ''.join( char for char in reversed(urlparse(url).netloc) )
        # Reversed to avoid e.g. cdn.website.pl > cookie.pl > website.pl
        return domain
    
    to_show = sorted( to_show,
                      key=lambda e: (e.browser, _get_domain(e.url), e.url) )
    for e in to_show: print(e)


def get_images( *args, **kwargs ):
    return get_entries( *args, **kwargs, extensions=IMAGE_FORMATS )


def extract_data( *args, entrylist=None,
                  images_only=False, folder=None, **kwargs ):
    '''Extracts binary data from an entry object'''

    if len(args) == 1 and not 'entrylist' in kwargs:
        entrylist = args[0]
    
    if folder: out_folder = folder
    else: out_folder = f'{DEFAULT_OUTPUT_FOLDER}_{int(get_time())}'
    out_folder = Path(out_folder).absolute()
    if not out_folder.exists(): out_folder.mkdir()

    f_tag = 'pliki'
    if images_only:
        extractable = get_images( *args, **kwargs )
        f_tag = 'obrazki'
    elif entrylist: extractable = entrylist
    else:
        extractable = get_entries( *args, **kwargs )
    
    for entry in extractable:
        try: entry.extract_data( out_folder )
        except OSError: pass
        except Exception as e: error(f'Błąd podczas wyciągania pliku: {e}')
        
    print(f'Przeniesiono {f_tag} ({len(extractable)}) do folderu:\n'
          f'{out_folder}')


def extract_images( *args, **kwargs ):
    extract_data( *args, **kwargs, images_only=True )


if __name__ == '__main__':

    # Tutaj możesz wkleić ścieżkę do folderu z pamięcią podręczną,
    # który chcesz sprawdzić (w takim wypadku musisz też podać nazwę
    # przeglądarki jako `CUSTOM_BROWSER`

    CUSTOM_PATH = ""

    # W tym miejscu możesz wpisać nazwę przeglądarki.
    # Jeśli tego nie zrobisz, to skrypt poszuka dla wszystkich, jakie zna.
    
    CUSTOM_BROWSER = ""

    # A tej funkcji poniżej najlepiej nie zmieniać ;)
    entries = get_cache_entries( cache_path=CUSTOM_PATH,
                                 browser=CUSTOM_BROWSER )

