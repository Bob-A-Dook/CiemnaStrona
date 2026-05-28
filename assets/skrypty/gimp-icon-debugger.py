'''
Looks inside Gimp's source code for the expected icons,
then compares the list to the icons inside the installed version
to see if any are missing
'''
import re
from pathlib import Path
from logging import error
from subprocess import run, PIPE


SOURCE_CODE_FOLDER = 'gimp-master'
GIMP_SOURCE_ICON_FILE = 'libgimpwidgets/gimpicons.h'
GIMP_INSTALLED_ICON_FOLDER = '/usr/share/gimp/3.0/icons/Default/scalable/apps'

# Add your own path if you want to put missing icons in a specific folder
CUSTOM_ICON_COPIES_FOLDER = ''

def get_necessary_files_and_folders():
    '''
    Checks if all hardcoded Gimp's files and folders exists. If not, gives
    the users advice on what to do
    '''
    gimp_source_folder = Path(SOURCE_CODE_FOLDER)
    if not gimp_source_folder.exists():
        error('\n'.join((
            'Folder with Gimp\'s source code not found! Either move the code '
            'to:', f'{gimp_source_folder.absolute()}', '',
            '...Or edit this script and set the variable:',
            'SOURCE_CODE_FOLDER = your/folder/path')))
        return

    icondef_file = gimp_source_folder / GIMP_SOURCE_ICON_FILE

    gimp_icon_folder = Path( GIMP_INSTALLED_ICON_FOLDER )
    if not gimp_icon_folder.exists():
        error('Folder with installed Gimp icons not found! Make sure that '
              'Gimp is installed on your system or manually change the path '
              'inside the script to:\n'
              'GIMP_INSTALLED_ICON_FOLDER = your/folder/path')
        return
    
    return icondef_file, gimp_icon_folder


def get_icon_names_from_source_code( icondef_file ):
    '''
    Parses the C header file containing the expected icon names
    (part of Gimp's source code) and creates a list of them all
    '''
    with open( icondef_file ) as f:
        definitions = []
        for line in f:
            if line.startswith('#define'):
                definitions.append( line )

    finder_re = re.compile(r'"(.*?)"$')
    icon_names = []
    for line in definitions:
        matched_name = finder_re.search( line.strip() )
        if matched_name:
            icon_names.append( matched_name.group(1) )

    return icon_names


def check_for_missing_icons( icon_names, gimp_icon_folder ):
    '''
    Compares the expected icon files from the source code with the
    ones actually present in installed Gimp's folders.
    '''
    # Standardize names to basic stems without extensions or additional info
    installed_icons = [ic.stem.replace('-symbolic','')
                       for ic in gimp_icon_folder.iterdir()
                       if ic.suffix == '.svg']
    iconset = set( installed_icons )
    
    missing_icons = []
    for iname in icon_names:
        if not iname in iconset:
            if iname == 'gimp-wilber': continue #Special case
            missing_icons.append( iname )

    return missing_icons


def _display_advice():
    print('', 'If you prefer a manual solution, you can look for the files '
          'listed above and put them inside the folder named above the list.',
          '(You can also use icon files without "-symbolic" in their names, '
          'especially if you changed Gimp\'s settings to avoid using them.',
          'It might also be possible to use .png files instead of .svg)',
          sep='\n')


def find_icon_replacements( missing_icons ):
    '''Searches all system files for the missing icons'''

    # Try updating the search index
    r = run('sudo updatedb'.split(' '), stderr=PIPE)
    if r.stderr:
        if b'sudo' in r.stderr:
            error('Cannot update search index! Use this script as admin:\n'
                  f'sudo python3 {__file__}')
            return
        else:
            error( r.stderr )
        return
    
    r = run('locate .svg'.split(' '), stdout=PIPE )
    lines = ((l, l.split(b'/')[-1]) for l in r.stdout.split(b'\n'))
    filenames = ((p, str(l, 'utf-8')) for p, l in lines)

    matcher = re.compile('({})'.format('|'.join( missing_icons ))).search
    candidates = [(p,fname) for p,fname in filenames if matcher( fname )]

    found = []
    for mi in missing_icons:
        for p, can in candidates:
            if mi+'-symbolic' in can:
                found.append( p ) #TODO: check other variations as fallback
                break # =move on to matching the other names

    return [str(p,'utf=8') for p in found]


def copy_icon_replacements_to_folder( replacements, icon_folder ):
    errors, copied = 0, 0
    for rep in replacements:
        r = run(f'cp {rep} {icon_folder}'.split(' '), stderr=PIPE)
        if r.stderr: errors += 1
        else: copied += 1
    print(f'Copied {copied} icons')
    if errors:
        error(f'{errors} errors')
        error('Failed to copy some files. Try running this script as root:\n'
              f'sudo python3 {__file__}')


def main():
    paths = get_necessary_files_and_folders()
    if not paths: return

    icondef_file, gimp_icon_folder = paths
    icon_names = get_icon_names_from_source_code( icondef_file )
    missing_icons = check_for_missing_icons( icon_names, gimp_icon_folder )

    if not missing_icons:
        print('No missing Gimp icons detected :)')
        return
    
    # Otherwise, show all missing icons and give some advice
    print('# MISSING ICONS #',
          'Some icons expected inside Gimp\'s code have not been found '
          'in your icon folder:', '',
          f'{gimp_icon_folder}', '', 'Their list:', '', sep='\n')

    for mic in missing_icons:
        print( f'{mic}-symbolic.svg', )

    print('\nDo you want to search for matching icons on your system?')
    inp = input('y if yes ')
    if inp.lower() == 'y':
        replacements = find_icon_replacements( missing_icons )
    else:
        _display_advice()
        return
    if not replacements: return

    # Some replacement icons have been found, suggest copying them
    if not CUSTOM_ICON_COPIES_FOLDER:
        icon_folder, desc = gimp_icon_folder, 'Gimp\'s folder'
    else:
        icon_folder = CUSTOM_ICON_COPIES_FOLDER
        desc = icon_folder
    
    print(f'{len(replacements)} replacement icons found. Want to copy '
          f'them to {desc}? (might require admin permission)')
    inp = input('y if yes ')
    if inp.lower() == 'y':
        iconp = Path( icon_folder )
        if not iconp.exists(): iconp.mkdir( parents=True, exist_ok=True )
        copy_icon_replacements_to_folder( replacements, icon_folder )
    

if __name__ == '__main__':
    
    main()
