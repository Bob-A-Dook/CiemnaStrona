'''
Skrypt odczytujący dane EXIF z plików z obrazkami.

Parts of code copied from:

https://stackoverflow.com/questions/4764932/
in-python-how-do-i-read-the-exif-data-for-an-image

and:

https://stackoverflow.com/questions/19804768/
interpreting-gps-info-of-exif-data-from-photo-in-python
'''
__author__ = 'Bob-A-Dook'
__email__ = "bob.adook@tutanota.com"
__license__ = "MIT"

###############################
# Imports and globals
###############################

from pathlib import Path
from pprint import pprint
from logging import error

KNOWN_IMAGE_TYPES = []
try:
    from PIL import Image, ExifTags
    
    KNOWN_IMAGE_TYPES = Image.registered_extensions().keys()
    EXIF_TAGS = ExifTags.TAGS
    GPS_TAGS = ExifTags.GPSTAGS
    
except ImportError: 
    error('Brak modułu `PIL`! Żeby skrypt działał, '\
          'zainstaluj go, wpisując w PowerShell `pip install pillow`')

EXIF_GPS_LABEL = 'GPSInfo'
EXIF_TIME_LABEL = 'DateTime'

OUT_NAME = 'metadane_exif.txt'

###############################
# Helper functions
###############################

def __is_image(file):
    '''Checks if the file type is a PIL-supported image'''
    return (Path(file).suffix.lower() in KNOWN_IMAGE_TYPES)


def __safe_error( template, *values ):
    try:
        print( template.format(*values) )
    except UnicodeEncodeError:
        raw_values = [bytes(v, encoding='utf-8') for v in values]
        error( template.format(*raw_values) )
        error('UWAGA! Nie da się wyświetlić nazwy pliku'\
              ' (zawiera emoji albo inne nieznane znaki).'\
              ' Odpal skrypt w innym programie, np. PowerShell.')


def _codes_to_labels( data, tags ):
    '''Assigns EXIF attribute codes (numbers) to readable names'''
    return {tags[number]: value
            for number, value in data.items()
            if number in tags}


def _convert_to_degrees(dms):
    """
    Helper function to convert the GPS coordinates stored in the EXIF
    to degress in float format.
    """
    # Some versions of PIL store GPS coordinates as tuples,
    # some use IFDRational class (or floats); handle all cases
    real_dms = []
    for coord in dms:
        if isinstance(coord, tuple):
            raw_coord, number = coord
            real_dms.append( raw_coord / number )
        else:
            real_dms.append(coord)
       
    d,m,s = real_dms 
    return d + (m / 60.0) + (s / 3600.0)


def _get_readable_location(exif_gps_data):
    """
    Gets the latitude and longitude from EXIF data (if available) and
    returns it in a format supported by online maps search.
    """
    location_info = []
    for label in ('GPSLatitude', 'GPSLatitudeRef',
                  'GPSLongitude', 'GPSLongitudeRef'):
        try:
            loc = exif_gps_data[ label ]
            location_info.append( loc )
        except KeyError:
            error('Brak pełnych danych o lokalizacji!')
            return
   
    gps_lat, gps_lat_ref, gps_long, gps_long_ref = location_info
    
    lat = _convert_to_degrees(gps_lat)
    if gps_lat_ref == 'S':
        lat *= -1

    lon = _convert_to_degrees(gps_long)
    if gps_long_ref == 'W':
        lon *= -1

    return lat, lon

###############################
# Class for EXIF data
###############################

class ExifData:
    
    __slots__ = ['filename', 'data', 'location', 'time']

    def __init__(self, filename, raw_exif_data):

        self.filename = filename
        self.data = _codes_to_labels( raw_exif_data, EXIF_TAGS )
        self.location = None
        self.time = None

        try:
            gps_info = self.data[ EXIF_GPS_LABEL ]
            gps_info = _codes_to_labels( gps_info, GPS_TAGS )
        except KeyError: pass
        else:
            self.data[ EXIF_GPS_LABEL ] = gps_info
            self.location = _get_readable_location( gps_info )

        try:
            self.time = self.data[ EXIF_TIME_LABEL ]
        except KeyError: pass
            

    def save_to_file(self, open_file):

        print_to_file = lambda *text: print(*text, file=open_file, sep='\n')

        decoration = '#'*30 
        print_to_file( decoration, self.filename, decoration )

        pprint( self.data, stream=open_file)

        if self.time:
            print_to_file('','CZAS:\n{}'.format(self.time), '')
        
        if self.location:
            readable_loc = str(self.location).strip('() ')
            print_to_file('LOKALIZACJA:\n{}'.format( readable_loc ), '' )
                  
###############################
# Main functions
###############################
        
def get_exif( image_path ):
    '''
    Opens an image file, checks for EXIF metadata and wraps it into
    an ExifData object.
    '''
    img = Image.open( image_path )
    raw_exif_data = img._getexif()

    if raw_exif_data is None: return
 
    return ExifData( image_path, raw_exif_data )


def get_exif_from_all( folder=None ):
    '''Gets EXIF data from all images in the folder'''

    if not KNOWN_IMAGE_TYPES: return

    if not folder:
        folder_path = Path.cwd() # Current directory
        out_name = OUT_NAME
    else:
        folder_path = Path(folder)
        out_name = folder + '_' + OUT_NAME

    print('','Sprawdzam obrazki w folderze "{}"...'.format(folder_path), '',
          sep='\n')

    image_files = sorted(f for f in folder_path.iterdir() if __is_image(f))
    if not image_files:
        error('W folderze nie ma (znanych rodzajów) obrazków!')
        return
    
    with open( out_name, 'w') as out:
        for image in image_files:
            try:
                exif_object = get_exif( image )
                if not exif_object: continue
                exif_object.save_to_file( out )
                
            except Exception:
                __safe_error(
                    'Nie udało się zapisać danych z obrazka "{}"! Błąd: "{}"',
                    image.name)

    print('Zapisano metadane do pliku "{}"'.format(out_name))


if __name__ == '__main__':

    folder = ""
    # Zamiast "" może być ścieżka do folderu (między cudzysłowami!)
    
    get_exif_from_all( folder )

    # Jeśli w folderze były jakieś obrazki, ich dane EXIF zostaną zapisane
    # do pliku tekstowego kończącego się na "metadane_exif.txt",
    # w tym samym folderze w którym jest skrypt
