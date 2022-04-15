'''
! This is a Polish version of the script. Only the code is in English,
  but all messages are in Polish.

Skrypt ułatwiający walkę z trollami szerzącymi dezinformację.
Można mu wrzucać linki do podejrzanych postów/komentarzy z Facebooka,
Twittera albo Nittera (albo całe komentarze, jako HTML w formie tekstu), 
a on skonwertuje je do postaci gotowej do wklejenia i otworzy stronę
"zglostrolla.pl" w domyślnej przeglądarce. 
Przez nią sami możemy wkleić link w odpowiednim polu.

W miarę możliwości skrypt korzysta z systemowego schowka. Ponadto może
zapisywać skopiowane linki i komentarze na naszym dysku.
Nie wymaga niczego poza podstawowym Pythonem, chyba że używamy go na
urządzeniu mobilnym (przez Termux). Więcej informacji w komunikatach. 
'''
__author__ = 'Bob Adook'
__mail__ = 'bob.adook@tutanota.com'


import re
from time import time
from pathlib import Path
from sys import argv, modules
from urllib.parse import urlparse
from html.parser import HTMLParser
from shutil import which as program_exists
from logging import warning, error, exception, basicConfig
from webbrowser import (open as website_open, get as get_browser,
                        register as register_browser)

# Custom logging messages
basicConfig( format='[%(levelname)s]: %(message)s' )

RUNS_ON_TERMUX_WITH_CLIPBOARD = False
Tk = None
try:
    from tkinter import Tk
except ImportError:
    if all([program_exists('termux-clipboard-'+t) for t in ('get', 'set')]):
        RUNS_ON_TERMUX_WITH_CLIPBOARD = True
        print('Wykryto, że skrypt działa w programie Termux i ma dostęp '
              'do schowka.\n[UWAGA] Upewnij się, że masz zainstalowaną apkę '
              '"Termux:API". Bez niej schowek się zawiesza.\nPonadto obie '
              'apki powinny być zainstalowane przez program "F-Droid".')

RUNS_IN_IDLE = ('idlelib' in modules)
PREVENT_WINDOW_FROM_CLOSING = not RUNS_IN_IDLE
DEBUG_MODE = False

ANTITROLL_WEBSITE = 'https://zglostrolla.pl#wpforms-submit-858'
DEFAULT_LOG_FOLDER = Path.home() / 'Documents/Antitroll'
SUPPORTED_DOMAINS = ('nitter.net', 'twitter.com', 'facebook.com')

################################
# Preparing the clipboard widget
################################

clipboard = None    
if Tk:
    # Create dummy Tk window for accessing clipboard
    try:
        clipboard = Tk()
        clipboard.withdraw()
    except Exception: pass

elif RUNS_ON_TERMUX_WITH_CLIPBOARD:
    # Special case, have to use Termux programs instead of Tk
    
    from subprocess import Popen, PIPE
    
    class TermuxClip:
        '''A separate clipboard widget for Termux (mobile terminal)''' 
        
        def clipboard_clear(self): pass
        
        def clipboard_get(self):
            program = ['termux-clipboard-get']
            p = Popen( program, stdout=PIPE, stderr=PIPE )
            out, err = p.communicate()
            return str(out, 'utf-8')
           
        def clipboard_append( self, text ):
            text = bytes(text, 'utf-8')
            program = ['termux-clipboard-set', text]
            p = Popen( program )
            p.wait()
            
    clipboard = TermuxClip()

if not clipboard:
    error('Brak możliwości dostępu do schowka! Program jest w stanie jedynie '
          'wyświetlać link i otwierać okno ze stroną do zgłaszania trolli')

###########################################################
# Preparing the command for opening the default web browser
###########################################################

try: default_browser = get_browser()
except Exception:
    if program_exists('termux-open'):
        register_browser("termux-open '%s'", None)
        print('Skrypt użyje w roli przeglądarki komendy z Termuxa\n')
    else:
        error('Nie wykryto domyślnej przeglądarki, skrypt nie będzie w stanie '
              'automatycznie otwierać strony "zglostrolla.pl"')

##############################################
# General functions for clipboard interactions
##############################################

def _get_clipboard_content():
    content = ''
    try:
        content = clipboard.clipboard_get()
    except Exception as e:
        if ("selection doesn't exist" in str(e)):
            error('W schowku nie było tekstu')
        elif ("selection owner didn't respond" in str(e)):
            error('Schowek nie odpowiada (może się tam znajdować duży '
                  'plik, na przykład obrazek zamiast tekstu)')
        else: error('Nieznany błąd podczas wyciągania treści ze schowka!')

    return content


def _add_link_to_clipboard( link ):
    success = True
    try:
        clipboard.clipboard_clear()
        clipboard.clipboard_append( link )
    except Exception:
        error('Nie udało się umieścić linku w schowku')
        success = False
        
    return success


def _check_content_type( content ):
    '''Checks whether the clipboard content was a link or HTML code''' 
    if '<' in content and '>' in content: _type = 'html'
    else: _type = 'link'
    return _type

######################################
# Handling HTML strings from clipboard
######################################

class LinkParser(HTMLParser):
    '''A parser for finding links inside basic HTML'''

    website_url = ''
    links = []
    
    def handle_starttag(self, tag, attrs):
    
        if tag == 'meta':
            for attr,value in attrs:
                if attr == 'content':
                    self.website_url = value.strip("'")
        elif tag == 'a':
            for attr, value in attrs:
                if attr in ('href', 'data-uri'):
                    print(value)
                    if value.startswith('/'): # Relative link
                        u = urlparse( self.website_url )
                        value = f'https://{u.netloc}{value}'
                        print('Amended: ', value)
                    self.links.append( value )

    
def __find( pattern, text ):
    p = re.search( pattern, text )
    if p: return p.group(0)
    else: return ''

    
def _get_link_from_html( html:str ):
    '''
    Parses HTML in form of a string (from DevTools or the SelSword
    extension) in order to get the link to content.
    '''
    print('W schowku znajdował się fragment strony internetowej')
    parser = LinkParser()
    parser.feed( html )
    
    author_url = parser.website_url
    u = urlparse( author_url )
    sitename = f'{u.scheme}://{u.netloc}'

    has_link_to_itself = False
    chosen_link = None
    for link in parser.links:

        if link == '#': has_link_to_itself = True

        if 'm.facebook.com' in link or 'm.facebook.com' in sitename:
            chosen_link = _handle_mobile_facebook_link( link, author_url )

        elif 'story_fbid=' in link and '&id=' in link:
            # Special case on www.facebook.com (with permalink.php) or
            # classic m.facebook.com / mbasic.facebook.com
            linkpath = _parse_numeric_id_link( link )
            if not sitename:
                if 'entstream' in link: sitename = 'https://m.facebook.com'
                else: sitename = 'https://mbasic.facebook.com'
            chosen_link = sitename + linkpath

        elif 'www.facebook.com' in link:
            com_id = __find( 'comment_id=[0-9]+(&|$)', link )
            if not com_id: com_id = __find( 'posts/([0-9]+)', link )
            if com_id:
                chosen_link = link
            
        elif 'nitter.net' in link:
            if link.endswith('#m'): chosen_link = link

        elif 'twitter.com' in link and re.search( 'status/[0-9]+', link):
            chosen_link = link
        
        elif link.startswith('/'):
            # Should only happen if text was copied from DevTools;
            # The SelSword extension would add the original page url
            chosen_link = _handle_relative_link( link )
            
        if chosen_link: break
                
    if not chosen_link:
        error('W kodzie HTML nie znaleziono linku w odpowiednim formacie')
        if has_link_to_itself:
            print('Możesz jednak spróbować najechać kursorem na datę posta, '
                  'a potem skopiować go ponownie. Jest szansa, że wtedy '
                  'strona załaduje element z linkiem.\n')

    return chosen_link


def _handle_relative_link( link ):
    '''If there is no domain in the link, look at its parameters'''
    chosen_link = None
    if link.endswith('#m'):
        chosen_link = 'https://nitter.net' + link      
    elif re.search( 'status/[0-9]+', link):
        chosen_link = 'https://twitter.com' + link

    return chosen_link


def _parse_numeric_id_link( link ):
    '''
    Some FB links have "X.php?id=Y..." instead of readable identifiers.
    In such cases, the links have to be constructed in a different way.
    '''
    story_id = re.search('story_fbid=[0-9]+', link).group(0)
    main_id = re.search('&id=[0-9]+', link).group(0)
    comm_id = __find('&comment_id=[0-9]+', link)
    rep_id = __find('&reply_comment_id=[0-9]+', link)
    return urlparse(link).path + '?' + story_id + main_id + comm_id + rep_id


def _handle_mobile_facebook_link( link, post_author_url ):
    '''
    There are no direct links to comments on m.facebook.com (mobile), so
    the information has to be extracted from link parameters.
    The assembled link is in desktop browser format.
    '''
    TOKEN, ID = 'parent_redirect_comment_token', 'reaction_comment_id'
    STORY_ID = 'story_fbid'
    if not ((TOKEN in link and ID in link) or (STORY_ID in link)): return

    if STORY_ID in link and '&id=' in link:
        #Special case; this link has numeric IDs, so extract them
        link_path = _parse_numeric_id_link( link )
        return 'https://m.facebook.com' + link_path

    if not post_author_url:
        error('We wklejonym tekście nie było linku do całego posta. Musisz '
              'wkleić go ręcznie (albo nacisnąć Enter, żeby zakończyć)')
        post_author_url = inp('Link do głównego posta: ')
        if not post_author_url: return

    user = urlparse( post_author_url ).path.strip('/')

    params = [param.split('=') for param in urlparse( link ).query.split('&')]
    post_id, comm_id, reply_id = '','',''
    for param in params:
        if len(param) == 1: continue #Like the standalone 'snowflake' attr
        attr, value = param
        if attr == TOKEN: post_id, comm_id = value.split('_')
        elif attr == ID: reply_id = value
        elif attr == STORY_ID: post_id = value

    if reply_id == comm_id: reply_id = ''
    
    optional_comm_id, optional_reply_id = '', ''
    if comm_id: optional_comm_id = f'?comment_id={comm_id}'
    if reply_id: optional_reply_id = f'&reply_comment_id={reply_id}'
    
    link = (f'https://www.facebook.com/{user}/posts/{post_id}'
            f'{optional_comm_id}{optional_reply_id}')

    return link


def _add_link_as_text_fragment():
    '''
    When all else fails and no link to content can be extracted, at
    least give an URL to top-level content along with the comment
    author's name.
    '''
    pass #TODO


def __prettify_html( html: str ):
    return re.sub( '<', '\n<', html )

################################
# Formatting the extracted links
################################

def get_link():
    '''
    Gets the link to the troll's post or comment. If it's not
    provided as an argument, it can be fetched from clipboard.
    '''
    link, html = '', ''

    # First, check for command line arguments (in shell only)
    if not RUNS_IN_IDLE:
        try: link = argv[1]
        except Exception: pass
        else: return _clean_link( link ), html

    # Then try getting the link via clipboard
    if USE_CLIPBOARD:
        print('\nWyciąganie zawartości schowka...')
        text = _get_clipboard_content()   
        ctype = _check_content_type( text )
        if ctype == 'link': link = text
        elif ctype == 'html':
            html = text
            link = _get_link_from_html( html )
                
        if link: return _clean_link( link ), html

    # As a last resort, prompt for user input
    print('[ENTER żeby zakończyć albo wklej link do posta/komentarza]\n')
    link = input( 'LINK: ')
    if not link: return
    return _clean_link( link ), html


def _clean_link( link ):
    '''
    Removes junk in case of Facebook links; swaps Nitter with Twitter
    in case of Nitter links.
    '''
    try: u = urlparse( link )
    except Exception: u = link, link = link.geturl()
    
    if not all( (u.scheme, u.netloc, u.path) ):
        if len(link) > 200: link = link[:200] + '...'
        error(f'\n("{link}")\n\n^ Ten tekst nie jest poprawnym linkiem '
              'ani fragmentem strony!\n'
              'Przykład dobrego linku: https://www.facebook.com/stronka\n')
        link = ''
    
    NITTER, TWITTER, FACEBOOK = SUPPORTED_DOMAINS

    if NITTER in link:
        link = link.replace( NITTER, TWITTER )
        link = re.sub( '#m$', '', link )
    elif FACEBOOK in link:
        link = re.sub( '\?*&*__cft__.*$', '', link )
    elif TWITTER in link:
        link = re.sub( '\?.*$', '', link ) #Remove all parameters

    return link


def launch_antitroll():
    '''
    The core of the program. Gets and formats a link to a troll's post
    (either from clipboard HTML, command line or directly pasted),
    opens the website for reporting trolls and saves supplementary data.
    '''
    if '-d' in argv:
        argv.remove('-d')
        DEBUG_MODE = True
        
    data = get_link()
    if not data: return
    link, html = data
    if not link:
        error('Brak linku do wklejenia na stronę')
        return

    text = 'LINK DO SKOPIOWANIA NA STRONĘ'
    if USE_CLIPBOARD and clipboard:
        link_in_clip = _add_link_to_clipboard( link )
        if link_in_clip:
            text = 'UMIESZCZONO W SCHOWKU LINK'
    
    information = f'\n{text}:\n{link}\n'
    print( information )

    if DEBUG_MODE: return # Do not save anything or open browser
    website_open( ANTITROLL_WEBSITE )

    log_folder = _get_log_folder()
    curtime = int(time())
    
    if SAVE_LINKS_TO_LIST:
        save_link_to_log( link, log_folder, curtime )
    if html and SAVE_ORIGINAL_COMMENTS:
        save_comment( html, link, log_folder, curtime )

    if PREVENT_WINDOW_FROM_CLOSING: input('[Naciśnij ENTER, żeby zakończyć] ')

#################################
# Saving links and whole comments
#################################

def _get_log_folder():
    if CUSTOM_LOG_FOLDER: log_folder = CUSTOM_LOG_FOLDER
    else: log_folder = DEFAULT_LOG_FOLDER
    if not log_folder.exists(): log_folder.mkdir( parents=True )
    return log_folder

    
def save_link_to_log( link, log_folder, curtime ):
    '''
    If everything goes OK, a timestamp and link are saved to a log file
    for future reference.
    '''    
    log_file = log_folder / 'troll_log.txt'
    text = f'{curtime}\t{link}\n'
    with open( log_file, 'a', encoding='utf-8') as out:
        out.write( text )
        print(f'Dodano link do pliku zbiorczego:\n{log_file}\n')


def save_comment( html_comment, link, log_folder, curtime ):
    '''Saves the whole comment's HTML to a file fur further analysis'''

    comment_file = log_folder / f'{curtime}.html'
    html_comment = __prettify_html( html_comment )

    domain = urlparse(link).netloc
    css_file = f'./{domain}.css'
    css_tag = f'<link rel="stylesheet" type="text/css" href="{css_file}"/>'

    html_comment = (f'<html>\n<head>\n{css_tag}\n</head>\n'
                    f'<body>\n{html_comment}\n</body>\n</html>')
            
    with open( comment_file, 'w', encoding='utf-8') as outf:
        outf.write( html_comment )
        print(f'Zapisano cały komentarz do pliku:\n{comment_file}\n')
        print('[UWAGA] Zapisany plik HTML może, oprócz trolla, zawierać dane '
              'identyfikujące użytkownika tego skryptu (np. link do awatara '
              'na Facebooku). Proszę zachować ostrożność w przypadku '
              'udostępniania go innym osobom.\n')

if __name__ == '__main__':

    # W tym miejscu możesz ustawić (zmieniając True na False), czy chcesz
    # żeby program brał link ze schowka i go do niego odkładał po obróbce 
    USE_CLIPBOARD = True

    # Czy chcesz żeby program otworzył stronę do zgłaszania trolli
    # w domyślnej przeglądarce
    AUTO_WEBSITE_OPEN = True

    # Czy chcesz zapisywać linki do trolli do jednego zbiorczego pliku
    SAVE_LINKS_TO_LIST = True

    # Czy chcesz zapisywać również całe ich komentarze w formacie HTML
    # (działa tylko po ich uprzednim skopiowaniu do schowka)
    SAVE_ORIGINAL_COMMENTS = True

    # Tutaj między cudzysłowami możesz wpisać pełną ścieżkę do folderu
    # na zapisywane pliki (listę linków i treść komentarzy)
    CUSTOM_LOG_FOLDER = "" #Path.home() / 'Documents/Wojna/Trolle/LOG'

    # Tego poniżej nie ruszaj ;)
    launch_antitroll()
    
