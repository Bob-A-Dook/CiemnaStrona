"""
A module for getting and analyzing all Messenger messages written by a single
person. Just launch it in the same folder as the zip with JSON data
downloaded from Facebook. A summary of statistics and a chronological list
of messages will be created in the same folder.

ATTENTION! The script is adapted to JSON-format data from Facebook
and does not support HTML (the default download format).

Some code chunks were inspired by StackOverflow answers:

Fixing Facebook's encoding:
https://stackoverflow.com/questions/50008296/
facebook-json-badly-encoded?noredirect=1&lq=1

Printing emoji as Unicode:
https://stackoverflow.com/questions/
25707222/print-python-emoji-as-unicode-string

Regex for finding emoji taken from:
https://gist.github.com/Alex-Just/e86110836f3f93fe7932290526529cd1

Another regex idea for more sophisticated emoji:
https://blog.geooff.com/2021/01/plucking-emoji-from-strings-in-python.html

If you want to analyze something yourself, you can do:

```
import messenger_stats as ms
name, msgs = ms.get_all_messages()
```
Optionally provide a name, e.g. `get_all_messages( 'Justin Case' )`,
to get all by Justin Case.

Then work on `msgs`, a list of Message objects. Some examples below.

To get posts longer than 200 characters:

`posts = [m for m in msgs if len(m.text) > 200]`

To get posts from 2020 someone reacted to:

```
posts = [m for m in msgs if m.reactions
         and _timestamp_to_time( m.timestamp, t='year' ) == 2020]
```
"""
__author__ = 'Bob-A-Dook'
__mail__ = 'bob.adook@tutanota.com'
__license__ = 'MIT'

from pathlib import Path
from zipfile import ZipFile
from collections import Counter
from re import (split as re_split, findall as re_findall,
                compile as re_compile, escape as re_escape)
from json import (load as json_load, dump as json_dump)
from logging import error, warning
from datetime import datetime
from statistics import mean, median

EMOJI_MODULE = False
try:
    import emoji
    EMOJI_FIXER = lambda text: emoji.demojize( text, use_aliases=True )
    EMOJI_MODULE = True
except ImportError:
    EMOJI_FIXER = lambda text: text.encode('unicode-escape')

#################################
# General globals
#################################

# Folder names
MESSAGE_FOLDER = 'messages'


# Conversation attribute names
PARTICIPANTS = 'participants'
NAME = 'name'
ALL_MESSAGE_DATA = 'messages'

# Attributes in raw message data
MSG_SENDER = 'sender_name'
MSG_TIME = 'timestamp_ms'
MSG_TEXT = 'content'
MSG_REACTIONS = 'reactions'
MSG_UNSENT = 'is_unsent'
MSG_TYPE = 'type'

R_EMOJI = 'reaction'
R_PERSON = 'actor'

BASIC_MSG_PROPERTIES = (MSG_SENDER, MSG_TIME, MSG_TEXT,  MSG_REACTIONS,
                        MSG_UNSENT, MSG_TYPE)

SPECIAL_MSG_PLACEHOLDERS = {
    'photos': '<ZDJĘCIA>',
    'sticker': '<NAKLEJKA>',
    'files': '<PLIKI>',
    'gifs': '<GIFY>',
    'videos': '<FILMY>',
    'share': '<LINK>',
    'audio_files': '<NAGRANIE GŁOSOWE>',
    'call_duration': '<POŁĄCZENIE>',
    'users': '<INTERAKCJE>'
    }

# Output files
INDEX_FILE = 'index.json'

# Regexes
EMOJI_RE = re_compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "\U000024C2-\U0001F251" 
    "]+"
)

EMOJI_SHORTCUTS = [':)',':(',';)', ':D', ';(', ':/',':|',
                   ':p', ':o', '^_^', '8)']
TEXT_EMOJI_RE = re_compile( '({})'.format(
    '|'.join( re_escape(es) for es in EMOJI_SHORTCUTS)))

TOKENIZER_RE = re_compile('[.,;:()!?/*" ]+')
TOKENIZE = lambda text: TOKENIZER_RE.split( text )

# Displayed messages
NO_ATTR_ERROR = '''
Plik z danymi nie zawiera atrybutu "{}", tak jak powinien.
Jeśli powtórzy się to przy wielu plikach, to być może Facebook
zmienił nazewnictwo. W takim wypadku daj znać, np. na bob.adook@tutanota.com.
'''

# Text templates
DATE_TEMPLATE = '%Y-%m-%d %H:%M:%S'
REPORT_DATE_TEMPLATE = '%d.%m.%Y %H:%M:%S'

# HTML report template
LOGO = '''
<svg viewBox="0 0 24 24" width="80" height="80" stroke-linecap="round">
 <circle fill="#0026c4" stroke="#4bc9c8" cx="12" cy="12" r="10"/>
 <path d="M 6 14 a 10 20 0 0 0 12 0" stroke="#bad2f9" fill="none"/>
 <path d="M 6 9 a 10 70 1 0 1 4 0" stroke="#bad2f9" fill="none"/>
 <path d="M 14 9 a 10 70 1 0 1 4 0" stroke="#bad2f9" fill="none"/>
</svg>
'''
BAR_COLOR = '#4bc9c8'
HEADER = ('<div class="h">\n{}\nStatystyki<br/>z Messengera</div>'.format(LOGO))
SUBTITLE = '<p class="small">Zebrane skryptem z '\
           '<a href="https://www.ciemnastrona.com.pl">Ciemnej Strony</a></p>'
TITLE = '<h1>{}</h1>' 
TABLE_ROW = '<tr><td class="first-col">{}</td><td class="last-col">{}</td></tr>'
HTML_TEMPLATE_START = '''<!DOCTYPE html><html lang="pl">
<head>
 <style>
 .main {background-color: #252525; color:#ddd; font-family:sans-serif}
 .small {font-size: 15.75px; color: #828282} 
 h2 {font-weight:400; margin-top: 30px; margin-bottom: 30px}
 svg {display:inline-block; margin-right:10px}
 h1 {font-weight:600;margin-top:2em}
 .last-col {white-space:nowrap; vertical-align:bottom}
 .h {color:#4bc9c8; font-weight:bold; font-size:26px;
     display:flex;align-items:center} a {color: #5e8fee;text-decoration:none}
 td {padding:10px; line-height:1.3; vertical-align:top}
 text {fill:#ddd} line{stroke-width: 20}
 </style>
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <meta charset="utf-8">
</head>
<body class="main">'''
HTML_TEMPLATE_END = '</body></html>'

######################################
# Emoji printing support and fallbacks
######################################

def __test_emoji_support( display=False ):
    '''Tests if the current terminal is capable of displaying emoji'''
    if not display: return True

    encoded_emoji = u'\U0001f604'
    print('\nTest emoji...')
    try:
        print( 'Można wyświetlać emoji! '+encoded_emoji+'\n')
        print( 'UWAGA: Jeśli wyświetla się nieprawidłowo, to najlepiej '\
              'użyć innego terminala')
        return True  
    except UnicodeEncodeError:
        warning('Twój obecny terminal nie wyświetla poprawnie emoji.'\
                'Najlepiej użyj innego, takiego jak PowerShell.\n')
        return False

is_imported = (__name__ != '__main__') # Skip further checks if just importing
CAN_DISPLAY_EMOJI = __test_emoji_support( display=is_imported )
if not CAN_DISPLAY_EMOJI and not EMOJI_MODULE:
    warning('Nie znaleziono modułu `emoji`, ich opisy nie będą wyświetlane. '\
            'Można go pobrać przez `pip install emoji`.)')

        
def _prepare_emoji_for_print( text: str ):
    '''
    Adapts a string of text to the current terminal, depending on whether
    it supports emoji and if the `emoji` module was installed:
    
    1. Tries to keep the original text, including emoji
    2. If emoji module was imported, it tries to replace emoji with names
    3. Tries to replace emoji with their raw unicode
    4. If all else fails, replaces text with an error message.
    '''
    if CAN_DISPLAY_EMOJI: return text
    try:
        text_to_show = EMOJI_FIXER( text )
    except Exception:
        text_to_show = (
            'UWAGA! Nie da się wyświetlić tekstu'\
            ' (zawiera emoji albo inne nieznane znaki).'\
            ' Odpal skrypt w innym programie, np. PowerShell.')      
    return text_to_show

###################################
# Helper functions for loading data
###################################

def _fix_text_encoding( msg_text: str ):
    return msg_text.encode('latin_1').decode('utf-8')


def __format_num( number ):
    '''Formats long numbers by inserting spaces inside them'''
    number = str(number)
    if len(number) <= 4 or not number.isnumeric(): return number
    new = []
    for i, n in enumerate(reversed(number)):
        if i % 3 == 0: new.append(' ') #Divisible by 3
        new.append( n )
    return ''.join( reversed(new) )


def _load_messages( message_file, msg_dir,
                    name_to_get=None, as_raw_data=False ):
    '''
    Used by all to load the lists of messages
    from the specified JSON file (in Facebook's format).
    '''
    if isinstance(msg_dir, ZipFile):
        data = json_load(
            msg_dir.open( message_file ))
    else:
        with open(message_file) as f:
            data = json_load(f)
    
    try:
        messages = data[ ALL_MESSAGE_DATA ]
    except KeyError:
        error(NO_ATTR_ERROR.format( ALL_MESSAGE_DATA ))
        return []
    
    if name_to_get:
        messages = [m for m in messages
                    if _fix_text_encoding(m[ MSG_SENDER ]) == name_to_get]

    if not as_raw_data:
        messages = [Message(msg_data) for msg_data in messages]
        
    return messages


def _timestamp_to_time( timestamp, t=None ):
    '''
    Gets data from a timestamp - either a complete date and time
    or a specified part (e.g. hour only)
    '''
    date = datetime.fromtimestamp( timestamp )
    if t: date = getattr( date, t )
    return date
        

def _parse_message_data( data, name_only=False ):
    '''
    Gets data from a single Facebook message.
    This includes time, text, sender names and additional items
    (photos, videos, stickers etc.).
    '''    
    try:
        sender = _fix_text_encoding( data[ MSG_SENDER ] )
        if name_only: return sender
        timestamp = data[ MSG_TIME ] // 1000      
    except KeyError as e:
        # Should not occur unless FB changes variable names
        return

    # Get message text
    try:
        text = _fix_text_encoding( data[ MSG_TEXT ] )
    except KeyError:
        text = ''

    # Get reactions  
    try:
        reactions = data[ MSG_REACTIONS ]
        for r in reactions:
            r[ R_EMOJI ] = _fix_text_encoding( r[ R_EMOJI ] )
            r[ R_PERSON ] = _fix_text_encoding( r[ R_PERSON ] )
    except KeyError:
        reactions = None

    # Get additional attachments
    alt = ''
    special = {k:v for (k,v) in data.items()
               if not k in BASIC_MSG_PROPERTIES}
    for attr_name, attr_value in special.items():
        try:
            alt = SPECIAL_MSG_PLACEHOLDERS[ attr_name ]
        except KeyError:
            alt = '<UNKNOWN TYPE: {}>'.format(attr_name)
        break

    # Mark if message was unsent
    try:
        if data[MSG_UNSENT]: alt = '<USUNIĘTA>'
    except KeyError: pass

    # Treat text about interactions as alt text, not main
    attachments = special
    if alt == '<INTERAKCJE>':
        alt, text = text, ''
           
    return (sender, timestamp, text, attachments, reactions, alt)

#################################
# Main classes for data
#################################

class Message:
    '''
    A single message containing text, a timestamp and perhaps
    some attachments and reactions.
    '''
    __slots__ = ['text', 'timestamp', 'sender',
                 'attachment', 'reactions', 'alt']

    def __init__(self, data):
        
        msg_info = _parse_message_data( data )
        (self.sender,
         self.timestamp,
         self.text,
         self.attachment,
         self.reactions,
         self.alt) = msg_info
            
    def __str__(self):
        
        date = _timestamp_to_time( self.timestamp )
        readable_date = date.strftime( DATE_TEMPLATE )

        text = self.text
        if not self.text: text = self.alt
        
        text_to_show = _prepare_emoji_for_print( text )

        if self.reactions:
            reactions = ''.join(r[ R_EMOJI ] for r in self.reactions)
            reactions = '\n| ' + _prepare_emoji_for_print( reactions )
        else:
            reactions = ''
                
        return ('<{0} | {1} | {2} {3}>'.format(
            self.sender, readable_date, text_to_show, reactions ))

    def __repr__(self):
        return self.__str__()

##############################################
# Functions for loading conversations and messages
##############################################

def __get_message_dir():
    '''
    Gets the directory with Messenger messages. Should be robust
    in case the user is already deeper in the hierarchy or hasn't unpacked
    the zip file.
    '''
    msg_dir = None
    curdir = Path()

    zipfiles = []
    for path in curdir.rglob('*'):
        if path.is_dir() and path.name == MESSAGE_FOLDER:
            msg_dir = path
            break
        elif path.suffix == '.zip':
            zipfiles.append( path )

    if msg_dir: return msg_dir

    # Else: check if data can be loaded straight from zip
    try:
        zf = ZipFile( zipfiles[0] ) # Only tries one
        print('UWAGA: Dane ładowane prosto z pliku zip')
        return zf
    except IndexError:
        pass
            
    # Else: check if user is already deeper inside the inbox directory
    dir_parts = curdir.absolute().parts
    if MESSAGE_FOLDER in dir_parts:
        index = dir_parts.index( MESSAGE_FOLDER ) + 1
        dir_parts = dir_parts[ :index ]
        msg_dir = Path( *dir_parts )
        return msg_dir
    else:
        error('Nie znaleziono folderu z wiadomościami! Upewnij się, że '\
              'odpalasz skrypt w odpowiednim folderze')
        return None
            

def get_all_message_files():
    '''Gets all possible messages in JSON format from the message directory'''
    ATTACHMENT_FOLDER = 'files'

    msg_dir = __get_message_dir()
    if not msg_dir: return ([], None)

    if isinstance(msg_dir, ZipFile):
        file_list = [Path(p) for p in msg_dir.namelist()]
        file_list = [p for p in file_list if MESSAGE_FOLDER in p.parts]
    else:
        file_list = msg_dir.rglob('*')
        
    is_attachment = lambda p: p.parent.name == ATTACHMENT_FOLDER
    json_files = [str(p.as_posix()) for p in file_list
                  if p.suffix == '.json' and not is_attachment(p)]

    return (json_files, msg_dir)


def _get_from_zipfile( zipped_files, file_paths ):
    '''Gets all files with a specific relative path from a zipped file'''
    msg_dir = ZipFile( zipped_files)

    # Construct a regex for files which end with the right path
    file_re = re_compile(
        '({})$'.format( '|'.join( file_paths )))

    matching_files = [f for f in msg_dir.namelist() if file_re.search(f)]
    return matching_files


def _get_paths_from_index( name ):
    
    with open(INDEX_FILE) as ind:
        index = json_load(ind)
        msg_dir, name_index = index['dir'], index['names']
        
    if not name:
        print('Nie podano imienia, biorę osobę najczęstszą w konwersacjach')
        name_count = sorted( [item for item in name_index.items()],
                             key = lambda x: len(x[1]),
                             reverse=True)
        name = name_count[0][0] #Person inside most conversations
  
    try:
        files_to_get = name_index[name]
        
        if msg_dir.endswith('.zip'):
            message_files = _get_from_zipfile( msg_dir, files_to_get )
        else:
            message_files = [Path(p) for p in files_to_get]
            
    except Exception as e:
        return (name, '', [])
    
    print('Załadowano z indeksu konwersacje dla "{}" (łącznie {})'
          .format( name, len(message_files) ))
    print('\nUWAGA: Gdyby coś się zmieniło w folderze z wiadomościami, to '\
          'usuń stary indeks (plik "{}")\n'.format( INDEX_FILE ))
        
    return (name, msg_dir, message_files)

    
def _create_index():
    '''Creates a new index matching users to conversations (JSON files)'''
    message_files, msg_dir = get_all_message_files()
    if not message_files: return
    
    print('Brak indeksu, tworzę nowy. To może chwilę potrwać...')
    name_index = {}
    for f in message_files:
        messages = _load_messages( f, msg_dir, as_raw_data=True )
        senders = list(set( _parse_message_data(m, name_only=True)
                            for m in messages ))
        for sender in senders:
            path = str(f)
            try: name_index[sender].append( path )
            except KeyError: name_index[sender] = [path]

    if isinstance( msg_dir, ZipFile): msg_dir = msg_dir.filename
    if not name_index: return
    
    index = {'dir': str(msg_dir), 'names': name_index}
    with open( INDEX_FILE, 'w') as out: json_dump( index, out, indent=2 )
    print('Stworzono nowy indeks dla {} użytkowników'.format(len(name_index)))
    return index


def __remove_duplicates( messages ):
    unique = set()
    duplicates = set()
    skipped_num = 0
    
    for m in messages:
        msg_info = ( m.text, m.timestamp )
        if msg_info in unique:
            skipped_num += 1
            duplicates.add( msg_info )
            continue
        else:
            unique.add( msg_info )

    messages = [m for m in messages
                if not (m.text, m.timestamp) in duplicates]
    if skipped_num:
        print('Ominięto powtórzone wiadomości ({})'.format( skipped_num ))
    return messages


def get_all_messages( name=None ):
    '''
    Guesses the main author (or accepts a provided name)
    and fetches all messages written by that person.
    '''
    try:
        file_info = _get_paths_from_index( name=name )
    except FileNotFoundError:
        index = _create_index()
        if not index: return (name, [])
        file_info = _get_paths_from_index( name=name )

    name, msg_dir, message_files = file_info

    if msg_dir.endswith('.zip'): msg_dir = ZipFile( msg_dir )
        
    if not message_files:
        error('Brak wiadomości od użytkownika "{}"'.format(name))
        return (name, [])
   
    all_messages = []
    for msg_f in message_files:
        try:
            messages = _load_messages( msg_f, msg_dir, name_to_get=name )
            all_messages += messages
        except Exception as e:
            error('Błąd przy ładowaniu pliku {}'.format(msg_f))
    
    all_messages = __remove_duplicates( all_messages )
    all_messages = sorted( all_messages, key=lambda msg: msg.timestamp )
    return (name, all_messages)

#################################
# Histogram preparation
#################################

def __fill_missing_labels( data, labels ):
    data_labels = [l for (l,_) in data]
    missing = [(l,0) for l in labels if not l in data_labels]
    data = [(label, 0) if label in missing else (label,value)
            for (label,value) in data]
    data += missing
    return data


def __change_starting_point( data, new_start, sorter_key ):
    '''Sorts the list according to a specified key and then rearranges
    it so that it starts at a new point'''
    try:
        data = sorted(data, key=sorter_key)
        return data[new_start:] + data[:new_start]
    except Exception:
        return data


def _make_histogram( data ):
    '''Creates a histogram for relative frequencies within the data'''
    SPACING = 30
    CHAR_WIDTH = 11 #Approximate
    BAR_WIDTH = 20
    TEXT_SPACE_H = 50
    VERTICAL_SPACING = 20
    MAX_BAR_HEIGHT = 400
    SVG_TEMPLATE = '<svg viewBox="0 0 {} {}" style="max-width:800px">'\
                   '{}</svg>'.strip()
    SVG_BAR = '<line stroke="{col}" '\
              'x1="{x}" y1="{bottom}" x2="{x}" y2="{top}"></line> '
    SVG_BAR_TEXT = '<text x="{text_x}" y="{text_y}">{text}</text>'

    data = __fill_missing_labels( data, range(24) )
    data = __change_starting_point( data, 5, sorter_key=lambda x: x[0])

    labels, values = zip(*data)
    x_ticks = [SPACING + i*SPACING for i in range(len(data)+1)]     
    label_x_ticks = [x - ( len(str(l)) * CHAR_WIDTH / 2 )
                     for x,l in zip(x_ticks, labels)]

    # Get relative frequencies and scale bars upwards to fill the area
    total_v = sum(values)
    bar_tops = [v / total_v * MAX_BAR_HEIGHT for v in values]    
    scale_factor = MAX_BAR_HEIGHT / max(bar_tops)
    bar_tops = [bt * scale_factor for bt in bar_tops]

    # Fill all templates with the formatted info
    bars = [ SVG_BAR.format(
        x=x, bottom=MAX_BAR_HEIGHT, top=MAX_BAR_HEIGHT-value, col=BAR_COLOR)
             for (value, x) in zip(bar_tops, x_ticks)]
    
    labels = [ SVG_BAR_TEXT.format( text=text,
        text_x=text_x, text_y=MAX_BAR_HEIGHT+VERTICAL_SPACING)
               for (text, text_x) in zip(labels, label_x_ticks)]
    bars = '\n'.join( bars+labels )
    
    graph_width = max(label_x_ticks) + SPACING
    graph_height = MAX_BAR_HEIGHT + TEXT_SPACE_H
    svg = SVG_TEMPLATE.format( graph_width, graph_height, bars )
    return svg


#################################
# Basic conversation analysis
#################################

def get_base_stats( messages ):
    '''Gets basic information: message number, date of first and last'''
    format_date = lambda m: (_timestamp_to_time(m.timestamp)
                             .strftime( REPORT_DATE_TEMPLATE )
                             .replace(' ','<br/>'))
    first_time = format_date( messages[0] )
    last_time = format_date ( messages[-1] )

    return ('Informacje podstawowe', (
            ('Liczba wysłanych wiadomości: ', len(messages)),
            ('Data pierwszej wiadomości: ', first_time),
            ('Data ostatniej wiadomości: ', last_time)
            ))


def count_message_hours( messages ):
    '''Gets hours at which a specific message was sent'''
    times = [_timestamp_to_time( m.timestamp) for m in messages]
    hours = [t.hour for t in times]
    sorted_hours = _sorted_count(hours)
    hours = [('{}:00'.format(h), c) for (h,c) in sorted_hours]

    at_work = [t for t in times if t.weekday() < 5 and (8 <= t.hour <= 16)]
    at_work = len(at_work)
    at_work_p = at_work / len(messages)

    try: hour_histogram = _make_histogram( sorted_hours )
    except Exception: hour_histogram = 'BŁĄD W TWORZENIU'

    return ('Godziny wysłania', (
              ('Wysłane w godzinach i dniach roboczych: ', at_work),
              ('%', at_work_p),
              ('Liczba wiadomości według godziny wysłania:', hours),
              ('[H] Wykres częstości według godzin:', hour_histogram)
              ))
                   

def count_reactions( messages ):
    '''Counts all different types of reactions the user's messages got'''
    reaction_msgs = [m for m in messages if m.reactions]
    if not reaction_msgs: return None
    
    all_reaction_data = [r_data for m in reaction_msgs
                         for r_data in m.reactions]
    actors = [r_data[ R_PERSON ]
              for r_data in all_reaction_data]
    reactions = [r for r_data in all_reaction_data
                 for r in r_data[ R_EMOJI ]]

    actor_count = _sorted_count( actors )
    reaction_count = _sorted_count( reactions )

    return ('Otrzymane reakcje', (
              ('Liczba wszystkich reakcji: ', len(reactions)),
              ('Liczba reakcji według rodzaju: ', reaction_count),
              ('20 najczęściej reagujących osób: ', actor_count[:20]),
              ('Liczba osób, które dały reakcję: ', len(actor_count))
              ))


def get_text_statistics( messages ):
    '''Gets statistics related to character and word count'''
    msgs_with_text = [m.text for m in messages if m.text]
    msg_lens = [len(text) for text in msgs_with_text]
    total_len = sum(msg_lens)
    average_len = int( mean(msg_lens))
    median_len = int( median( msg_lens ))

    all_words = [ TOKENIZE(text) for text in msgs_with_text]
    word_num_per_msg = [len(words) for words in all_words]
    average_word_num = int( mean( word_num_per_msg ))
    median_word_num = int( median( word_num_per_msg ))
    
    all_words = [w.lower() for words in all_words for w in words
                 if w.isalpha()]
    total_word_num = len( all_words )                 
    unique_words = sorted(list(set(all_words)))

    return ('Długość wiadomości', (
            ('Przeciętna długość wiadomości (w&nbsp;znakach): ', average_len),
            ('50% wiadomości ma więcej znaków&nbsp;niż: ', median_len),
            ('Liczba unikalnych słów: ', len(unique_words)),
            ('Przeciętna liczba słów w&nbsp;wiadomości: ', average_word_num),
            ('50% wiadomości ma więcej słów&nbsp;niż: ', median_word_num)
            ))

    
def count_emoji( messages ):
    '''Counts all emoji contained in message text'''
    all_emoji_m = [m for m in messages
                   if EMOJI_RE.search(m.text) or TEXT_EMOJI_RE.search(m.text)]
    
    emoji = [e for m in messages for e in EMOJI_RE.findall(m.text)]
    t_emoji = [e for m in messages for e in TEXT_EMOJI_RE.findall(m.text)]
        
    emoji_msg_num = len( all_emoji_m )
    emoji_msg_percent = emoji_msg_num / len(messages)
    unique_emoji_num = len(list(set( emoji + t_emoji )))
    emoji_count = _sorted_count( emoji )

    return ('Wysłane emoji', (
              ('Liczba wiadomości zawierających emoji: ', emoji_msg_num),
              ('%', emoji_msg_percent),
              ('Emoji w formie skrótu (np.&nbsp;^_^): ', len(t_emoji)),
              ('Emoji dodane jako obrazek: ', len(emoji)),
              ('Liczba unikalnych ciągów emoji: ', unique_emoji_num),
              ('20 najczęściej wysyłanych ciągów emoji: ', emoji_count[:20])
              ))
    

def count_attachments( messages ):
    '''Counts all special messages which contain attachments'''
    attachments = [m.attachment for m in messages if m.attachment]
    format_name = lambda x: x.strip('<>').title()

    attachment_num = len(attachments)
    labeled_atts = []
    for a in attachments:
        a_name = [k for k in a.keys()][0]
        try: label = format_name( SPECIAL_MSG_PLACEHOLDERS[a_name] )
        except KeyError: label = 'Nieznany rodzaj'
        labeled_atts.append( label )

    return ('Załączniki', (
            ('Liczba wiadomości zawierających załączniki: ', attachment_num),
            ('Wiadomości według rodzaju załączników: ',
             _sorted_count( labeled_atts )),
            ))
         

def _sorted_count( item_list ):
    '''Sorts a list according to the number of specific items'''
    return sorted( [(a,b) for (a,b) in Counter(item_list).items()],
                   key = lambda x: x[1], reverse=True)


def _make_html_report( out, name, results ):
    '''Writes the results of the analysis to an HTML file'''
    
    out.write( '\n'.join(
        (HTML_TEMPLATE_START, HEADER, SUBTITLE, TITLE.format(name))))

    wrap = lambda name, tag: '<{0}>{1}</{0}>'.format(tag, name)
    float_to_percent = lambda f: '({:0.1f} %)'.format( f*100).replace('.',',')

    def make_table(data):
        rows = '\n'.join(TABLE_ROW.format(l,s) for (l,s) in data)
        return wrap( rows, 'table' )
    
    for res in results:
        if not res: continue
        heading, stats = res
        
        out.write( wrap(heading, 'h2'))

        # Format the data and sort into two types
        info_table = []
        other_info = []
        for label, result in stats:
            
            if type(result) == list: # Item counts (e.g. reactions)
                other_info.append(( wrap(label, 'p'), make_table(result)))
                
            elif label.startswith('[H] '): #SVG histogram
                other_info.append(( wrap(label.replace('[H] ',''), 'p'),
                                    result))
            else:
                if label == '%': # Percent for previous stat
                    f_num = float_to_percent( result )
                    info_table[-1][-1] += '<br/>'+f_num 
                else: # Normal label+number
                    f_num = __format_num( result )
                    info_table.append( [label, f_num] )

        # Write all stats into the file
        out.write( make_table( info_table ) )
        for label, data_html in other_info:
            out.write( label )
            out.write( data_html )
           
    out.write( HTML_TEMPLATE_END )


def get_message_statistics( messages, name=None ):
    '''
    Gets some statistics related to a specific user's conversations:
    * number of characters, words, emojis written
    * number of unique words
    * number of received reactions and reacting people
    * messages sent per time of day
    '''
    if not messages: return

    out_name = name.lower().replace(' ','_')
    with open( out_name+'_wszystkie.txt', 'w', encoding='utf-8') as out:
        all_as_text = [str(m) for m in messages]
        out.write('\n\n'.join(all_as_text))
        print('Zapisano wszystkie wiadomości w kolejności chronologicznej!')

    analyzers = (get_base_stats, get_text_statistics, count_message_hours,
                 count_attachments, count_reactions, count_emoji)

    all_results = []
    for analyzer in analyzers:
        try:
            results = analyzer( messages )
        except Exception as e:
            fname = analyzer.__name__
            error('Błąd podczas użycia funkcji "{}"'.format(fname))
            continue
        else: all_results.append( results )
        
    with open(out_name+'_raport.html', 'w', encoding='utf-8') as out:
        _make_html_report( out, name, all_results )
        print('Zapisano statystyki dotyczące wiadomości!')

tok = TOKENIZE
        
if __name__ == '__main__':

    name = ""

    name, messages = get_all_messages( name=name )
    get_message_statistics( messages, name )
