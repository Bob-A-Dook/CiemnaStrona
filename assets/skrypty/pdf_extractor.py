'''
! This is the Polish version of this module. Only the code is in English. 

Skrypt przystosowany do struktury dokumentów finansowych
pobranych ze strony Ministerstwa Sprawiedliwości
(https://ekrs.ms.gov.pl/rdf/pd/search_df).
Wyciąga z plików XML załączone PDF-y zakodowane w formacie base64.
Następnie umieszcza je w osobnym folderze "pdfs".
'''

__author__ = 'Bob Adook'
__mail__ = 'bob.adook@tutanota.com'
__license__ = 'MIT'

# ^ In short: just use it however you want ;) No strings attached.
# However, I take no responsibility for anything you do.

import re
from logging import warning, error, exception
from pathlib import Path
from base64 import b64decode

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None
    warning('Brak modułu dodatkowego BeautifulSoup. Program spróbuje '
            'wyciągnąć dane jako tekst, ale może się to nie udać!\n'
            'Aby zainstalować BS, wpisz w konsoli '
            '"pip install beautifulsoup4", a potem '
            '"pip install lxml"\n')


def _bs_extract( xml_file ):
    '''Extracts PDFs from XML using the BeautifulSoup module.'''

    content = BeautifulSoup( open(xml_file, 'rb'), 'xml' )
    
    E_NAME = 'Zalacznik'
    E_ATTRS = {'format':'application/pdf'}

    internal_pdfs = [e for e in content.find_all( E_NAME, E_ATTRS)]

    pdfs = []
    for attachment in internal_pdfs:
        pdf = attachment.find('DaneZalacznika').text
        pdf = b64decode(pdf)
        pdfs.append( pdf )

    return pdfs


def _regex_extract( xml_file ):
    '''Extracts PDFs. Fallback in case BeautifulSoup is not installed.'''

    with open( xml_file, 'rb') as f:
        xml = f.read()

    pattern = (re.escape(b'<str:Zalacznik ')
               + b'.*?'
               + re.escape(b'</str:Zalacznik'))
    
    attachments = re.findall( pattern, xml, re.DOTALL )

    pdfs = []
    for att in attachments:
        is_pdf = (b'format="application/pdf"' in att)
        if is_pdf:
            pdf = re.search(b'DaneZalacznika\>(.*?)\<', att).group(1)
            pdf = b64decode(pdf)
            pdfs.append( pdf )

    return pdfs


def extract( xml_file, out_folder ):
    '''Uses either XML parsing or regex to extract embedded PDF files.'''
    
    try:
        if BeautifulSoup:
            pdfs = _bs_extract( xml_file )
        else:
            pdfs = _regex_extract( xml_file )
    except Exception:
        exception(f'Błąd podczas wyciągania plików z "{xml_file}"')
        return

    if not pdfs:
        print(f'[INFO] W pliku "{xml_file.name}" nie znaleziono PDF-ów')
        return

    for i, pdf in enumerate(pdfs):
        if i == 0: number = ''
        else: number = f'_{i}'

        pdf_name = f'{Path( xml_file ).stem}{number}.pdf'
        pdf_path = out_folder / pdf_name
        with open( pdf_path, 'wb' ) as out:
            out.write( pdf )

    return len(pdfs)    

        
def extract_all( folder_path=None ):
    '''Extracts PDF files from all XML files within a folder.'''

    if folder_path:
        folder = Path( folder_path )
        if not folder.exists():
            error(f'Nie udało się znaleźć folderu: "{folder_path}". '
                  'Najlepiej zostaw na końcu tego skryptu "folder = \'\' ", '
                  'a pliki XML wrzuć do tego samego folderu co skrypt.')
            return        
    else:
        folder = Path()
        
    xml_files = [f for f in folder.iterdir() if f.suffix.lower() == '.xml']
    if not xml_files:
        warning(f'W folderze "{folder.absolute()}" nie znaleziono plików XML')
        return

    out_folder = folder / 'pdfs'
    try: out_folder.mkdir()
    except FileExistsError: pass

    saved_num = 0
    for f in xml_files:
        saved_num = extract( f, out_folder )
        if saved_num:
            print(f'Wyciągnięto PDF-y (liczba: {saved_num}) z pliku "{f.name}"')

    if not saved_num: return
    print('\nWszystkie pliki przeniesiono do folderu:\n'
          f'{out_folder.absolute()}')


if __name__ == '__main__':

    # W tym miejscu można wpisać ścieżkę do jakiegoś folderu;
    # jeśli tego nie zrobimy, to skrypt poszuka w tym samym folderze,
    # w którym go odpaliliśmy
    
    folder = ""

    # Tego poniżej nie ruszamy :)
    extract_all( folder_path=folder )
