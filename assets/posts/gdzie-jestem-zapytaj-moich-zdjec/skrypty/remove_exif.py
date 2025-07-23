'''
Skrypt usuwający metadane EXIF ze wszystkich obrazków znajdujących się
w folderze. Tworzy nowy podfolder z kopiami obrazków pozbawionymi metadanych.
'''
__author__ = 'Bob-A-Dook'
__email__ = "bob.adook@tutanota.com"
__license__ = "MIT"

###############################
# Imports and globals
###############################

from pathlib import Path
from logging import error

KNOWN_IMAGE_TYPES = []
try:
    from PIL import Image
    KNOWN_IMAGE_TYPES = Image.registered_extensions().keys()
except ImportError:   
    error('Brak modułu `PIL` do otwierania obrazków! Żeby skrypt działał, '\
          'zainstaluj go, np. wpisując `pip install pillow` '\
          'w Powershella (na Windowsie)')

OUT_FOLDER = 'Bez_metadanych'
IMAGE_QUALITY = 95

###############################
# Helper functions
###############################

def __safe_error( template, *values ):
    try:
        print( template.format(*values) )
    except UnicodeEncodeError:
        raw_values = [bytes(v, encoding='utf-8') for v in values]
        error( template.format(*raw_values) )
        error('UWAGA! Nie da się wyświetlić nazwy pliku'\
              ' (zawiera emoji albo inne nieznane znaki).'\
              ' Odpal skrypt w innym programie, np. PowerShell.')


def __is_image(file):
    return (Path(file).suffix.lower() in KNOWN_IMAGE_TYPES)


def __prepare_image( filepath ):
    try:
        image = Image.open( filepath )   
    except Exception:
        __safe_error('Błąd przy ładowaniu obrazka "{}"', filepath.name)
        return None
    return image


def __prepare_out_path( image_path, out_folder_path ):

    image_name = image_path.name 
    out_path = out_folder_path.joinpath( image_name )
    
    if out_path.is_file():
        __safe_error(
            'Obrazek "{}" już jest w folderze, nie nadpisuję!', image_name)
        return None
    return out_path

###############################
# Main function
###############################

def strip_exif_from_images( folder=None ):
    '''
    Creates a copy of all images within the folder, with stripped
    EXIF metadata.
    '''
    if not folder:
        folder_path = Path.cwd() # Current directory
    else:
        folder_path = Path( folder )
    
    image_files = sorted(f for f in folder_path.iterdir() if __is_image(f))
    if not image_files:
        print('Brak (znanych rodzajów) obrazków w folderze "{}"!'
              .format(folder_path))
        return
    
    out_folder_path = folder_path.joinpath( OUT_FOLDER )
    out_folder_path.mkdir( exist_ok=True )

    n = 0
    for image_path in image_files:
        no_exif_image = __prepare_image( image_path )
        if not no_exif_image: continue

        out_path = __prepare_out_path( image_path, out_folder_path )
        if not out_path: continue
        
        no_exif_image.save( out_path, quality=IMAGE_QUALITY )
        n += 1
    print('Usunięto metadane z {} obrazków'.format(n))


if __name__ == '__main__':

    folder = ""
    strip_exif_from_images( folder )

    # W folderze, w którym odpalono skrypt powstanie folder "Bez_metadanych".
    # Będą w nich kopie obrazków, tyle że z usuniętymi danymi EXIF
    # Jeśli chcemy dodatkowo je skompresować, to można zmienić wartość
    # "IMAGE_QUALITY" w pierwszych linijkach skryptu (domyślna to 95).
