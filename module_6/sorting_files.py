from datetime import datetime
from pathlib import Path, PosixPath, WindowsPath
from sys import argv
from shutil import unpack_archive
import re


# Decorator for file type constants.
def constant(f):
    def fset(self, value): raise TypeError
    def fget(self): return f()
    return property(fget, fset)


# Classes for choosing constants 'all', 'files', 'dirs'
class TypeOfShowObject(object):
    @constant
    def ALL(): return 'all'
    @constant
    def FILES(): return 'files'
    @constant
    def DIRS(): return 'dirs'
    @constant
    def ERROR(): return 'error'


typeObj = TypeOfShowObject()

def del_empty_dirs(path, sort_dirs):
    """Recursively deleting empty directories in the target directory path.
    
    Key arguments:
    path - the directory in which the deletion will be carried out.
    sort_dirs is a list of directory names to be skipped anyway. 
    """
    for f in path.rglob('*'):
        if f.is_dir() and not (list(f.iterdir()) or f.name in sort_dirs):
            f.rmdir()
            return del_empty_dirs(path, sort_dirs)


def move_archives(root_dir, file_name):
    """Unpacking the archive into the root_dir directory and then deleting the original archive.
    
    Key arguments:
    root_dir is the directory into which the archive will be unpacked.
    file_name is the name of the archive. 
    """
    if root_dir.joinpath(file_name.stem).exists():
        unpack_archive(file_name, root_dir.joinpath(f"{file_name.stem}_{str(datetime.now().microsecond)}"))
    else:
        unpack_archive(file_name, root_dir.joinpath(f"{file_name.stem}"))
    # Delete the original archive file file_name.
    file_name.unlink()


def move_media(root_dir, file_name):
    """Transferring the file using the 'media' tag to the root_dir directory.
    
    Key arguments:
    root_dir is the directory into which the archive will be unpacked.
    file_name is the name of the source file.
    """
    if root_dir.joinpath(file_name.name).exists():
        # Move file_name to root_dir using filename + time in milliseconds.
        file_name.replace(root_dir.joinpath(f"{file_name.stem}_{str(datetime.now().microsecond)}{file_name.suffix}"))
    else:
        file_name.replace(root_dir.joinpath(file_name.name))


def normalize(in_str):
    """Replacing all characters except Latin and numbers in the transmitted string with Latin and '_'.
    
    Key arguments:
    in_str - the string to be modified.
    """
    global map_cyr_to_latin
    # Preparing a template for replacing non-latin characters, numbers and '_'.
    rx = re.compile(r"[^\w_]")
    # We transliterate the Cyrillic alphabet into Latin
    # and replace all symbols except Latin letters and numbers with '_'.
    return rx.sub('_', in_str.translate(map_cyr_to_latin))


def get_dir_obj(path, ext='*', show_all_files_dirs=typeObj.ALL, categories_list=[]):
    """We search recursively in the passed directory for files, directories or files or directories,
    skipping directory names from the passed categories.

    Key arguments:
    path is the target directory in which we are looking for objects.
    ext - the extension of the files that will appear in the output (without dots).
    show_all_files_dirs - which objects to display in the output: ALL, FILES or DIRS.
    categories_list - a list of directories that will not be searched. 
    """
    if not isinstance(path, (PosixPath, WindowsPath)):
        return (typeObj.ERROR, 'path must be a PosixPath or WindowsPath')
    try:
        if show_all_files_dirs in [typeObj.ALL, typeObj.DIRS] and path.is_dir():
            yield (typeObj.DIRS, path)
        for sys_obj in path.iterdir():
            if sys_obj.is_dir():
                # If the directory name is not in the list of categories.
                if sys_obj.name not in categories_list:
                    sys_obj = sys_obj.rename(sys_obj.with_name(normalize(sys_obj.name)))
                    yield from get_dir_obj(sys_obj, ext=ext, show_all_files_dirs=show_all_files_dirs, categories_list=categories_list)
            else:
                sys_obj = sys_obj.rename(str(sys_obj.with_name(normalize(sys_obj.stem)))+sys_obj.suffix)
                if sys_obj.match('**'+ext) and show_all_files_dirs in [typeObj.ALL, typeObj.FILES]:
                    yield (typeObj.FILES, sys_obj)
    except FileNotFoundError as e:
        if e.errno == 2:
            print(typeObj.ERROR, 'No such file or directory')


def sort_dir(_dir):
    """Sorting files in the passed directory.

    Key arguments:
    _dir is the target directory in which we are looking for objects.
    """
    pictures_ext = ['bmp', 'jpeg', 'png', 'jpg', 'gif']
    movies_ext = ['avi', 'mp4', 'mov']
    documents_ext = ['pdf', 'doc', 'docx', 'txt']
    music_ext = ['mp3', 'ogg', 'wav', 'amr']
    archives_ext = ['zip', 'gz', 'tar']
    # Dictionaries for each category. The 'tag' key is used in file handling functions. (move_media, move_archives)
    pictures = {'name': 'Изображения', 'dir_name': 'images', 'ext': pictures_ext, 'sort': True, 'tag': 'media', 'files': []}
    movies = {'name': 'Видео', 'dir_name': 'video', 'ext': movies_ext, 'sort': True, 'tag': 'media', 'files': []}
    documents = {'name': 'Документы', 'dir_name': 'documents', 'ext': documents_ext, 'sort': True, 'tag': 'media', 'files': []}
    music = {'name': 'Музыка', 'dir_name': 'audio', 'ext': music_ext, 'sort': True, 'tag': 'media', 'files': []}
    archives = {'name': 'Архиы', 'dir_name': 'archives', 'ext': archives_ext, 'sort': True, 'tag': 'archive', 'files': []}
    unknown = {'name': 'Другое', 'dir_name': 'other', 'ext': [], 'sort': False, 'tag': 'other', 'files': [], 'dirs': []}
    extensions_list = {'known': [], 'unknown': []}
    categories = [pictures, movies, documents, music, archives, unknown]
    # Dictionary: directory_name and a list of category extensions.
    cat_dirs = {cat['dir_name']: cat['ext'] for cat in categories}
    # By extension, we determine the name of the directory in the categories.
    dir_of_category = lambda extension: ''.join([k for k,v in cat_dirs.items() if extension in v])
    # List of extensions by tag 'media' from the category dictionary.
    ext_media_list = []
    # List of extensions by tag 'archive' from the category dictionary.
    ext_archive_list = []
    for cat in categories:
        tag = cat['tag']
        for c in cat['ext']:
            if tag == 'media':
                ext_media_list.append(c)
            elif tag == 'archive':
                ext_archive_list.append(c)
    # Create subdirectories for the categories in the target directory.
    for dir_name in cat_dirs.keys():
        _dir.joinpath(dir_name).mkdir(parents=True, exist_ok=True)
    # We generate a list of files contained in the target directory.
    src_files_gen = get_dir_obj(_dir, show_all_files_dirs=typeObj.FILES, categories_list=cat_dirs.keys())
    # We sort the files: with the media and archive tags according to our own rules.
    for type_obj, path_name in src_files_gen:
        # If the object type is "error", print a message to the console and end the loop. 
        if type_obj == typeObj.ERROR:
            print(type_obj, path_name)
            return ''
        elif type_obj == typeObj.FILES:
            name_ext, ext = path_name.name, path_name.suffix[1:]
            # By the file extension path_name,
            # we determine the name of the directory into which we will move the files.
            cat_dir = dir_of_category(ext)
            # Add the found filenames to the list of files for a specific category.
            for cat in categories:
                if cat['dir_name'] == cat_dir:
                    cat['files'].append(name_ext)
            # If the file extension is in the list of extensions
            # (which means the calculated directory name for extensions! = ''). 
            if cat_dir:
                # If it is a file from the 'media' tag (document, music, video, image).
                if ext in ext_media_list:
                    move_media(_dir.joinpath(cat_dir), path_name)
                # If it is an archive (tag 'archive').
                elif ext in ext_archive_list:
                    move_archives(_dir.joinpath(cat_dir), path_name)
                # Add the file extension to the list of known extensions.
                if ext not in extensions_list['known']:
                    extensions_list['known'].append(ext)
            # If you find a file with an unknown extension.
            else:
                # Add the file extension to the list of unknown extensions.
                if ext not in extensions_list['unknown']:
                    extensions_list['unknown'].append(ext)
    # We delete empty directories in the target directory
    # (except directories for categories).
    del_empty_dirs(_dir, cat_dirs.keys())
    # Return the result of the program in a formatted form.
    res_out = f"The directory\n{_dir}\ncontains the following files:\n"
    for cat in [c for c in categories if c['sort'] == True]:
        res_out += f"{cat['name']:<12}: {', '.join(cat['files'])}\n"
    res_out += f"List of known extensions: {', '.join(extensions_list['known'])}\n"
    res_out += f"List of unknown extensions: {', '.join(extensions_list['unknown'])}\n"
    return res_out


# Character transcoding table.
TABLE_SYMBOLS = ('абвгґдеєжзиіїйклмнопрстуфхцчшщюяыэАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЮЯЫЭьъЬЪ',
                (*('abvhgde'), 'ye', 'zh', *('zyi'), 'yi', *('yklmnoprstuf'), 'kh', 'ts',
                'ch', 'sh', 'shch', 'yu', 'ya', 'y', 'ye', *('ABVHGDE'), 'YE', 'ZH', *('ZYI'),
                'Yi', *('YKLMNOPRSTUF'), 'KH', 'TS', 'CH', 'SH', 'SHCH', 'YU', 'YA', 'Y', 'YE',
                *('_'*4)))

# Converting the lookup table to a dictionary for the str.translate property.
map_cyr_to_latin = {ord(src): dest for src, dest in zip(*TABLE_SYMBOLS)}


if __name__ == "__main__":
    try:
        # Attention: If WinError 122 is thrown, then the path contains the wrong slashes. Necessary "/"
        _dir = Path(argv[1])
        if not _dir.is_dir():
            print("The program has stopped: The parameter passed is not a directory, or the directory does not exist.")
            exit()
    except IndexError:
        print("Fatal error: Use the target directory path parameter to run the program.")
        exit()
    except Exception as err:
        print(f"Fatal error: {str(err)}")
        exit()
    # Sorting target directory
    print(sort_dir(_dir))
