from pathlib import Path, PosixPath, WindowsPath
# from string import ascii_letters
import re


pictures_ext = ['jpeg', 'png', 'jpg']
movies_ext = ['avi', 'mp4', 'mov']
documents_ext = ['doc', 'docx', 'txt']
music_ext = ['mp3', 'ogg', 'wav', 'amr']
archives_ext = ['zip', 'gz', 'tar']

pictures = {'name': 'Изображения', 'dir_name': 'images', 'ext': pictures_ext, 'files': []}
movies = {'name': 'Видео', 'dir_name': 'video', 'ext': movies_ext, 'files': []}
documents = {'name': 'Документы', 'dir_name': 'documents', 'ext': documents_ext, 'files': []}
music = {'name': 'Музыка', 'dir_name': 'audio', 'ext': music_ext, 'files': []}
archives = {'name': 'Архиы', 'dir_name': 'archives', 'ext': archives_ext, 'files': []}
unknown = {'name': 'Другое', 'dir_name': 'other', 'ext': [], 'files': [], 'dirs': []}
categories = [pictures, movies, documents, music, archives, unknown]

def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()
    return property(fget, fset)


# class для выбора констант 'all', 'files', 'dirs'
class TypeOfShowObject(object):
    @constant
    def ALL():
        return 'all'

    @constant
    def FILES():
        return 'files'

    @constant
    def DIRS():
        return 'dirs'


typeObj = TypeOfShowObject()

table_symbols = ('абвгґдеєжзиіїйклмнопрстуфхцчшщюяыэАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЮЯЫЭьъЬЪ',
                 (*(u'abvhgde'), 'ye', 'zh', *(u'zyi'), 'yi', *(u'yklmnoprstuf'), 'kh', 'ts', 'ch', 'sh', 'shch', 'yu', 'ya', 'y', 'ye', *(u'ABVHGDE'), 'Ye', 'Zh', *(u'ZYI'), 'Yi', *(u'YKLMNOPRSTUF'), 'KH', 'TS', 'CH', 'SH', 'SHCH', 'YU', 'YA', 'Y', 'YE', *(u'_'*4)))
map_cyr_to_latin = {ord(src): dest for src, dest in zip(*table_symbols)}


def normalize(in_str):
    global table_symbols, map_cyr_to_latin
    rx = re.compile(r"[^\w_]")
    return rx.sub('_', in_str.translate(map_cyr_to_latin))


def get_files_recur(path, ext='*', show_all_files_dirs=typeObj.ALL, calls=1):
    if not isinstance(path, (PosixPath, WindowsPath)):
        print('ERROR:', 'path must be a PosixPath or WindowsPath')
        return False
    try:
        if show_all_files_dirs in [typeObj.ALL, typeObj.DIRS] and path.is_dir():
            yield ('dir', path)
        for sys_obj in path.iterdir():
            if sys_obj.is_dir():
                # если функция вызвана больше 1 раза или имя каталога не в списке категорий
                if sys_obj.name not in [cat['dir_name'] for cat in categories if cat['dir_name'] != 'other']:
                    if not list(Path(sys_obj).iterdir()):
                        try:
                            Path(sys_obj).rmdir()
                            parent_dir = sys_obj.parent
                            if not list(Path(parent_dir).iterdir()):
                                Path(parent_dir).rmdir()
                        except OSError:
                            print('WARNING:', f'The {sys_obj} directory is not empty')
                    else:
                        path = Path(Path.rename(sys_obj, Path.joinpath(sys_obj.parent, normalize(sys_obj.name))))
                        yield from get_files_recur(path, ext=ext, show_all_files_dirs=show_all_files_dirs, calls=calls+1)
            else:
                name, extension = sys_obj.stem, sys_obj.suffix
                path = Path(Path.rename(sys_obj, Path.joinpath(
                    sys_obj.parent, normalize(name)+extension)))
                if sys_obj.match('**'+ext) and show_all_files_dirs in [typeObj.ALL, typeObj.FILES]:
                    yield ('file', sys_obj)
    except FileNotFoundError as e:
        if e.errno == 2:
            print('ERROR:', 'No such file or directory')


_dir = Path(r"/home/user1/1. COURSES/goit_github/1.test_")
(Path(Path.joinpath(_dir, cat['dir_name'])).mkdir(parents=True, exist_ok=True) for cat in categories if cat['dir_name'] != 'other')
gen = get_files_recur(_dir)
for g in gen:
    g
