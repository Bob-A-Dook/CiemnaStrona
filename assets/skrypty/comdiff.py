'''
ENGLISH:
A script for finding out which comments below Facebook posts
have been hidden in its default "most relevant" view.
The code is in English, but all displayed messages are in Polish.

POLISH:
Ten skrypt pozwoli ci porównywać komentarze pod postami z Facebooka
w różnych trybach wyświetlania ('najpopularniejsze' albo 'wszystkie').
Działa tylko dla treści ze strony internetowej www.facebook.com,
angielskiej i polskiej wersji językowej

Aby go uruchomić, najpierw pobierz Pythona z oficjalnej strony
(https://www.python.org/downloads/).
Zaznacz w instalatorze opcję zainstalowania programu "pip".
Potem kliknij dwukrotnie plik ze skryptem albo uruchom go przez inny program
i postępuj zgodnie z wyświetlanymi w konsoli instrukcjami.
'''

__author__ = 'Bob Adook'
__mail__ = 'bob.adook@tutanota.com'
__license__ = 'MIT'

# ^ In short: just use it however you want ;) No strings attached.
# However, I take no responsibility for anything you do.

##########
# Imports and basic 
##########

import re
from time import time
from pathlib import Path
from logging import warning, error, exception, basicConfig
from shutil import which as program_exists
from urllib.parse import urlparse

basicConfig( format='\n%(message)s\n' )

def show( text ):
    print('', text, '', sep='\n')

ERR = ''

##################################
# Importing BeautifulSoup for HTML
##################################

BeautifulSoup, FeatureNotFound = None, None
try:
    from bs4 import BeautifulSoup, FeatureNotFound
except ImportError:
    ERR = ('[BŁĄD] Brak biblioteki BeautifulSoup! Bez niej nie uda się '
          'odczytać komentarzy z Facebooka. Aby ją zainstalować, '
          'wpisz w konsoli:\n\n'
          'pip install beautifulsoup4\na potem:\n'
          'pip install lxml')

# Check if Beautiful Soup works fine
if BeautifulSoup and FeatureNotFound:
    try:
        _ = BeautifulSoup( 'test', 'lxml' )
    except FeatureNotFound:
        ERR = ('[BŁĄD] Brak biblioteki LXML, bez niej nie uda się odczytać '
              'treści strony. Otwórz konsolę (na przykład PowerShell '
              'na Windowsie) i wpisz w nią:\n'
              'pip install lxml')
        
        BeautifulSoup = None

#############################
# Preparing clipboard getters
#############################

RUNS_ON_TERMUX_WITH_CLIPBOARD = False
Tk = None
try:
    from tkinter import Tk
except ImportError:
    if all([program_exists('termux-clipboard-'+t) for t in ('get', 'set')]):
        RUNS_ON_TERMUX_WITH_CLIPBOARD = True
        print('[INFO]\nWykryto, że skrypt działa w programie Termux i ma '
              'dostęp do schowka.\n\nUpewnij się, że masz też zainstalowaną '
              'apkę "Termux:API". Bez niej schowek się zawiesza.\n'
              'Zarówno Termux, jak i Termux:API trzeba zainstalować '
              'przez apkę F-Droid. Wersja z Play Store nie działa.')


def __prepare_clipboard_getter():
    '''
    Specifies different ways of getting clipboard content depending
    on the operating system.
    '''
    clipboard_get = None    
    if Tk:
        # Create dummy Tk window for accessing clipboard        
        clip = Tk()
        clip.withdraw()
        def clipboard_get():
            try:
                return clip.clipboard_get()
            except Exception as e:
                no_clip_text = "CLIPBOARD selection doesn't exist"
                if no_clip_text in str(e):
                    error('Schowek jest pusty')
                return ''


    elif RUNS_ON_TERMUX_WITH_CLIPBOARD:
        # Special case, have to use Termux programs instead of Tk
        
        from subprocess import Popen, PIPE                       
        def clipboard_get():
            program = ['termux-clipboard-get']
            p = Popen( program, stdout=PIPE, stderr=PIPE )
            out, err = p.communicate()
            return str(out, 'utf-8')
                
    return clipboard_get


clipboard_get = None
try: clipboard_get = __prepare_clipboard_getter()
except Exception as e:
    exception('Nieznany błąd!')
    error('Nieznany błąd podczas ustalania sposobu dostępu do schowka')

if BeautifulSoup and not clipboard_get:
    ERR = ('[BŁĄD] Brak możliwości dostępu do schowka! Program jest w stanie '
          'jedynie porównywać komentarze z plików HTML zapisanych na dysku')

######################
# Globals and settings
######################

LOADED_ALL_SUCCESSFULLY = all((BeautifulSoup,))

SAVE_REPORT = True
DEFAULT_SAVE_PATH = Path.home() / 'Documents/cenzura'

FB_CSS = '''
.fb-link {color:#050505; cursor:pointer; font-weight:600; text-decoration:none}
.fb-comment {border-radius: 18px; margin-top: 12px; margin-bottom: 12px;
  font-size: .9375rem; font-family: Helvetica,Arial,sans-serif;
  padding: 12px 8px 12px 8px; background-color: #f0f2f5; line-height: 1.34;
  max-width:100%}
'''

CENSOR_CSS = '''
.censored {border-left: 4px solid red; padding-left:10px !important}
.uncensored {padding-left: 14px} .reply {margin-left:30px}
'''

##############
# Parsing HTML
##############

def _remove_tracking_params( link ):
    '''Reconstructs a link by removing Facebook's tracking parameters'''
    
    l = urlparse(link)
    params = [p for p in l.query.split('&')
              if not p.startswith('__cft__[0]')
              and not p.startswith('__tn__')]
    params = '&'.join( params )
    params = f'?{params}' if params else ''
    purged = f'{l.scheme}://{l.netloc}{l.path}{params}'
    return purged
    

def _get_ids_from_link( link: str ):
    '''
    Extracts different types of a comment's IDs by parsing its link.
    Also removes Facebook's tracking params as a bonus
    '''
    l = urlparse(link)
    params = [p for p in l.query.split('&')
              if not p.startswith('__cft__[0]')
              and not p.startswith('__tn__')]

    # Get parent- and reply-level comment ids
    com_id, reply_id, short_id = '', '', ''
    for p in params:
        if not '=' in p: continue
        name, val = p.split('=') 
        if name == 'reply_comment_id': reply_id = val
        elif name == 'comment_id': com_id = val

    short_id = reply_id if reply_id else com_id

    # Reconstruct the link without tracking params
    params = '&'.join( params )
    params = f'?{params}' if params else ''
    purged = f'{l.scheme}://{l.netloc}{l.path}{params}'

    return purged, com_id, reply_id, short_id
    

class FbComment:
    '''Corresponds to a specific Facebook comment with a unique id'''

    def __init__(self, com_html: BeautifulSoup ):

        links = com_html.find_all( 'a', attrs={'href': True} )
        for l in links:
            link_data = _get_ids_from_link( l.attrs['href'] )
            clean_link, com_id, reply_id, short_id = link_data

            self.link = clean_link
            self.com_id = com_id
            self.reply_id = reply_id
            self.short_id = short_id
            self.html = com_html
            self.text = com_html.text

            self.summary = self.text

        unrollers = [
            d for d in com_html.find_all('div', attrs={'role':'button'})
            if d.text.strip() == 'Zobacz więcej']
        self.is_unrolled = not unrollers

    def __hash__( self ):
        # A way of spotting same comments regardless of their text
        # (which could be either trimmed or fully unrolled)
        return hash( self.short_id )

    def __str__( self ):
        return self.link

    def __repr__( self ):
        return self.link


def get_comments_from_file( file ):
    html = BeautifulSoup( open(file), 'lxml' )
    return get_comments( html )


def _text_to_html( text ):
    if isinstance( text, BeautifulSoup ): html = text
    else: html = BeautifulSoup( text, 'lxml' )
    return html


COMMENT_RE = re.compile('(komentarz|odpowiedź)')

def get_comments( html ):
    '''Uses BeautifulSoup to find individual comments'''

    coms = html.find_all('div', attrs={'aria-label':True, 'role':'article'})
    coms = [c for c in coms
            if COMMENT_RE.search( c.attrs['aria-label'].lower() )]
    if not coms:
        warn = 'Nie znaleziono żadnych komentarzy!'
        warning( warn )
    else: print(f'\n[OK]\nUzyskano komentarze! Ich liczba: {len(coms)}')

    coms = [ FbComment(c) for c in coms ]
    return coms


def _display_comment( i, comment ):
    text = comment.text
    text = re.sub('\n\n+', '\n', text)
    text = re.sub('  +', ' ', text)
    print(f'\nCENZUROWANY KOMENTARZ NR {i+1}:\n{comment.link}\n{text}\n\n')


def _choose_unrolled_comment( c, was_censored, relevant_comment_map ):
    '''If possible, grabs the unrolled version of the same comment'''
    no_unrolled_version = False
    if was_censored:
        if not c.is_unrolled: no_unrolled_version = True     
    else:
        if not c.is_unrolled:
            # Always choose the unrolled version if available
            other_c = relevant_comment_map[ c.link ]
            if other_c.is_unrolled:
                c = other_c
                print('Wybrano rozwiniętą wersję komentarza')
            else: no_unrolled_version = True

    return c, no_unrolled_version


def find_censored( post1, post2 ):
    '''
    Compares two lists of comments from the same post to see if they
    were censored.
    '''
    comments1 = post1.comments
    comments2 = post2.comments

    if len(comments1) == len(comments2):
        print('[OK]\nBrak różnicy między trybem zwykłym a cenzurowanym!')
        return []

    if len(comments1) > len(comments2):
        all_coms, reduced = comments1, comments2
    else:
        all_coms, reduced = comments2, comments1
    comments_chosen_by_fb = {c.link: c for c in reduced}

    not_unrolled_num = 0
    annotated = []
    for c in all_coms:
        was_censored = (c.link not in comments_chosen_by_fb)
        
        c, not_unrolled = _choose_unrolled_comment( c, was_censored,
                                                    comments_chosen_by_fb )
        if not_unrolled: not_unrolled_num += 1
            
        annotated.append( (c, was_censored) )

    if not_unrolled_num:
        warning('Niektóre komentarzy nie były rozwinięte, ich treść będzie '
                'niepełna')

    uncen_num = len(annotated)
    print(f'Wśród {uncen_num} komentarzy było '
          f'{uncen_num-len(reduced)} domyślnie ukrytych')
    return annotated


def _find_censored_in_files( file1, file2 ):
    print(f'Porównywanie komentarzy z plików:\n1. {file1}\n2. {file2}\n')
    comments1 = get_comments_from_file( file1 )
    comments2 = get_comments_from_file( file2 )
    return find_censored( comments1, comments2 )

#################################
# Saving comments as HTML on disk
#################################

def _hide_options_bar( comment ):
    '''Hides some controls which would be useless in an offline file'''
    options = comment.find('ul')
    if options: options.decompose()
    report_button = comment.find( True, attrs={'aria-haspopup':'menu'})
    if report_button: report_button.decompose()


def save_html_summary( annotated_comments, post1, post2 ):
    '''Saves censored comments to a file for further inspection'''
    
    short_author = '' #TODO: Get from main link
    filename = f'cenzura_{int(time())}.html'

    formatted = []
    for c, was_censored in annotated_comments:
        _hide_options_bar( c.html )
        text = str(c.html)
        c_class = 'fb-comment'
        if was_censored: c_class += ' censored'
        else: c_class += ' uncensored'
        if c.reply_id: c_class += ' reply'
        
        text = f'<div class="{c_class}">{text}</div>'
        formatted.append( text )
        
    formatted = '\n'.join( formatted )
    content = (f'<html>\n<head>\n'
               f'<style>{FB_CSS}\n{CENSOR_CSS}\n</style>\n'
               '<link rel="stylesheet" href="fb.css" type="text/css"/></head>'
               f'<body style="margin-left:10px;margin-right:10px">\n'
               f'{formatted}</body>\n</html>')

    outpath = DEFAULT_SAVE_PATH / filename
    if not outpath.parent.exists(): outpath.parent.mkdir()
    with open( outpath, 'w') as out: out.write( content )
    
    show(f'[OK]\nZapisano oznaczone komentarze do pliku:\n{outpath}')
    
###########
# Main loop
###########

def _prompt_for_local_file_choice():
    show('W folderze znaleziono więcej niż dwa pliki HTML. Wybierz, '
          'które z nich chcesz ze sobą zestawić')
    for i, f in enumerate(html_files):
        print( f'{i+1}: {f.name}')

    print('')
    choice = input('Wybierz plik: ')
    

def find_censored_in_files():
    '''
    Loads comments from local HTML files and searches for censored comments.
    '''
    MAX_FILES_TO_DISPLAY = 50

    folder = Path().absolute()
    html_files = [f for f in folder.iterdir() if f.suffix == '.html']
    if not html_files:
        warning(f'[BŁĄD] W aktywnym folderze:\n{folder}\n'
                'nie ma żadnych plików HTML.')
        return

    elif len(html_files) == 1:
        warning(f'[BŁĄD] W aktywnym folderze:\n{folder}\njest tylko jeden '
                'plik HTML. Trzeba tam skopiować też drugą wersję posta.')
        return

    elif len(html_files) == 2:
        f1, f2 = html_files

    else:
        chosen = _prompt_for_local_file_choice
        if not chosen: return
        f1, f2 = chosen

#####################
# Facebook post class
#####################

def _complete_relative_links( links_with_tags ):

    def _complete( link ):
        if link.startswith('/'):
            link = 'https://www.facebook.com'+link
        elif link.startswith(':///'):
            link = 'https://www.facebook.com'+link.replace('://','')
        return link

    return [(t, _complete(l)) for (t,l) in links_with_tags]


def _get_unique_links( links_with_tags ):
    
    unique, linkset = list(), set()
    for elem,link in links_with_tags:
        link = _remove_tracking_params( link )
        if link in linkset: continue
        linkset.add( link )
        unique.append( (elem,link) )

    return unique
    

def _find_link_to_main_post( links_with_tags ):
    '''
    Looks at all the links contained within a post to get the link
    to the post itself. In some cases, the exact link is not shown
    and it is necessary to look at the comments.
    '''
    post_link = None
    no_ref_to_main = False

    for elem, link in links_with_tags:

        if post_link: break

        if '/ads/about/' in link:
            post_link = 'AD' #Sponsored post, will have no link
            continue

        if link in ('#','://'):
            no_ref_to_main = True
            continue

        is_from_fb = ('facebook.com' in link)
        is_link_to_post = ('/posts/' in link or 'pfbid' in link)
        is_comment = ('comment_id' in link)
        
        if is_from_fb and is_link_to_post:
            if is_comment:
                post_link = _extract_main_post_link( link )
                warning(f'[UWAGA] Link do głównego posta nie był podany '
                        'wprost, został odczytany z komentarzy.\n')
            else:
                post_link = link
        
    return post_link


def _get_post_author( post_link, links_with_tags ):
    '''
    Gets the author of the post. Usually it's enough to just trim the
    post link, but it's more nuanced if it was published within a group.
    '''
    author = None
    if (not '/groups/' in post_link and '/posts/' in post_link):
        return re.sub('/posts/.*?$', '', post_link )

    for tag, link in links_with_tags:
        if link.startswith('/'):
            link = 'https://www.facebook.com'+link
        if '/groups/' in link and '/user/' in link:
            return link

    if not author: warning('Nie udało się ustalić linku do autora posta')
    return 'UNKNOWN'


def _extract_main_post_link( comment_link ):
    l = urlparse( comment_link )
    return f'{l.scheme}://{l.netloc}{l.path}'


def _get_post_data( post ):
    '''
    Gets data which identifies the first post so that the script can
    later warn about comment source mismatches.
    '''
    post_data = {'author':None, 'link': None}

    link_elems = post.find_all('a', attrs={'href':True})
    links_with_tags = [(le, le.attrs['href']) for le in link_elems]
    links_with_tags = _get_unique_links( links_with_tags )
    links_with_tags = _complete_relative_links( links_with_tags )

    post_link = _find_link_to_main_post( links_with_tags )    
    if not post_link: warning('Nie ustalono linku do posta')
    else:
        post_data['link'] = post_link
        print(f'Ustalony link do posta:\n{post_link}')
        
        author = _get_post_author( post_link, links_with_tags )
        post_data['author'] = author
        print(f'Ustalony link do autora posta:\n{author}')

    return post_data


class FacebookPost:
    '''A class corresponding to a Facebook post along with its comments'''

    def __init__(self, html_post ):
            
        data = _get_post_data( html_post )
        comments = get_comments( html_post )

        # Check if all comments under the post have been unrolled
        clickables = html_post.find_all('div', attrs={'role':'button'})
        rolled, rolled_replies = [], []
        for c in clickables:
            if 'Zobacz więcej komentarzy' in c.text:
                rolled.append( c )
            elif re.search('\d+ odpowiedzi', c.text):
                rolled_replies.append( c )

        warntext = ''  
        if rolled:
            warntext = 'Nie rozwinięto w pełni listy komentarzy.'
        if rolled_replies:
            warntext += '\nNie rozwinięto niektórych odpowiedzi.'
        if rolled or rolled_replies:
            warntext += ('\nProgram może nie znaleźć wszystkich schowanych '
                         'komentarzy')
        if warntext: show( warntext )

        self.html = html_post
        self.data = data
        self.comments = comments
        self.is_incomplete = (rolled or rolled_replies)

###############
# Sanity checks
###############

def _is_proper_html( html ):
    if not all(('<' in html, '>' in html)):
        first_line = html.split('\n')[0]
        if len(first_line) < 100: snippet = first_line
        else: snippet = first_line[ :97 ] + '...'
        error(f'[UWAGA] Zawartość schowka:\n\n"{snippet}"\n\nnie zawiera '
              'tagów, to nie kod HTML!')

        if not RUNS_ON_TERMUX_WITH_CLIPBOARD:
            show(
                '[PORADA] Upewnij się, że kopiujesz źródło strony, a nie '
                'zwyczajny tekst.\nW tym celu np. kliknij prawym przyciskiem '
                'myszy na treść posta, kliknij "Zbadaj", najedź na '
                'odpowiadający postowi element, kliknij prawym przyciskiem '
                'i wybierz opcję "Kopiuj zewnętrzny HTML".')
        return False
    return True

   
def _is_from_facebook( html ):
    '''Checks if the clipboard contents actually come from Facebook'''
    is_fb_post = ('facebook.com' in str(html))
    if not is_fb_post:
        error('Format się nie zgadza z oczekiwanym, możliwe że to nie '
              'jest post z Facebooka (albo FB zmienił kod strony). '
              'Spora szansa, że program nie zadziała poprawnie.')
    return is_fb_post
    

def _is_same_post( post1, post2 ):
    '''
    Looks at some of the post's data to check if it is the same one
    and the only difference is in the comments.
    '''
    is_same = (post1.data == post2.data)
    if not is_same:
        warning('Według skryptu to inny post z Facebooka niż poprzedni, '
                'wyniki mogą nie być miarodajne. Skrypt służy tylko do '
                'porównywania komentarzy w jednym i tym samym poście')
    return is_same
                

###########################
# The interactive interface
###########################

def _display_greeting():
    show('Witaj w programie ComDiff!\n'
         'Pozwoli Ci oznaczyć komentarze pod postami, które Facebook '
         'ukrył w trybie domyślnym.')

    _display_help()
          
    show('[UWAGA] Program działa tylko na stronie Facebooka w polskiej '
         'i angielskiej wersji językowej.')


def _display_help():
    show('SKRÓTY KLAWISZOWE:\n'
         'H - przypomnienie skrótów klawiszowych\n'
         'Q - wyjście z programu.\n'
         'Z - powrót do poprzedniego etapu.\n'
         'F - porównanie dwóch zapisanych plików HTML z aktywnego '
          'folderu zamiast ze schowka.')
    

def _prompt_for_input( post1, post2 ):
    '''
    Asks user for input. Shows different things depending on the
    current state.
    '''    
    if not post1:
        show('[1] Skopiuj do schowka źródło HTML jakiegoś posta '
              'z Facebooka i naciśnij Enter.')
    else:
        show('[2] Teraz wybierz opcję "Wszystkie komentarze" pod tym '
              'samym postem, skopiuj jego kod HTML i naciśnij Enter.')
        
    inp = input('> ')
    return inp


def _get_facebook_post( clip_text, post1 ):
    '''
    Converts clipboard text to a FacebookPost object, running some sanity
    checks along the way to see if it's valid
    '''
    if not clip_text: return
    if not _is_proper_html( clip_text ): return

    html = _text_to_html( clip_text )
    is_fb_html = _is_from_facebook( html ) # Allow, but warn user
    
    if post1:
        if post1.html == html:
            warning('[UWAGA] W schowku było dokładnie to samo co '
                    'poprzednio, nie przybyło nowych komentarzy. Pamiętaj, '
                    'że po rozwinięciu wszystkich komentarzy należy '
                    'ponownie skopiować kod HTML posta.')
            return
        _is_same_post( post1.html, html )

    # Try various ways of getting Facebook post (different formats on
    # timeline, on pages, depends on the method of copying HTML...)
    
    post = None
    if 'aria-posinset' in html.attrs: post = html

    if not post:
        post = html.find( True, attrs={'aria-posinset': True} )

    if not post:
        if ('role' in html.attrs and html.attrs['role'] == 'article'):
            post = html
        else: post = html.find('div', attrs={'role':'article'})
    
    if not post:
        post = html
        warning('[UWAGA] Nie znaleziono posta w odpowiednim formacie. '
                'Facebook mógł go zmienić. Program spróbuje poszukać '
                'tego co zwykle, ale może nie zadziałać.\n'
                'Dla pewności sprawdź, czy kopiujesz cały element '
                'zawierający post, a nie tylko pojedyncze komentarze')

    return FacebookPost( post )
    

def run_interactive_mode():
    '''
    A step-by-step way of comparing Facebook comments from the same post
    in different display modes. Requires the user to copy HTML content to
    the clipboard or to save it as files on disk
    '''
    _display_greeting()

    post1, post2 = None, None
    while True:

        inp = _prompt_for_input( post1, post2 ).lower()
        
        if inp == 'q':
            return
        elif inp == 'f':
            return find_censored_in_files()
        
        elif inp == 'z':
            post1 = None
            continue
        
        elif inp == 'h':
            _display_help()
            continue

        if not clipboard_get:
            error('Brak dostępu do schowka, program nie zadziała w tym '
                  'trybie.\nAle nadal możesz zapisywać pliki HTML w jednym '
                  'folderze i je ze sobą porównywać')
            return

        clip_text = clipboard_get()
        post = _get_facebook_post( clip_text, post1 )
        if not post: continue
            
        # Getting and analyzing posts along with their comments
        if not post1: post1 = post
        else: post2 = post
            
        if post1 and post2:
            censored = find_censored( post1, post2 )
            if censored and SAVE_REPORT:
                save_html_summary( censored, post1, post2 )

            show('[KONIEC] Możesz teraz nacisnąć Z, żeby wrócić do '
                 'poprzedniego kroku, albo Enter, żeby opuścić program.')
            inp2 = input('Twój wybór: ')
            if inp2.lower() == 'z':
                post2 = None
            else:
                return
    
    
if __name__ == '__main__':

    if ERR:
        error( ERR ) # Show close to the user, stop for a while
        input()
    
    if LOADED_ALL_SUCCESSFULLY:
        try: run_interactive_mode()
        except Exception:
            exception('Nieznany błąd!')
            error('[BŁĄD] Wystąpił nieznany błąd programu.')
            input()

    else:
        if ERR: pass
        else: input()
