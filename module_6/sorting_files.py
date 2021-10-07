from datetime import datetime
from pathlib import Path, PosixPath, WindowsPath
from sys import argv
from shutil import unpack_archive
from random import randint
import re

pictures_ext = ['bmp', 'jpeg', 'png', 'jpg', 'gif']
movies_ext = ['avi', 'mp4', 'mov']
documents_ext = ['pdf', 'doc', 'docx', 'txt']
music_ext = ['mp3', 'ogg', 'wav', 'amr']
archives_ext = ['zip', 'gz', 'tar']

pictures = {'name': 'Изображения', 'dir_name': 'images',
            'ext': pictures_ext, 'sort': True, 'files': []}
movies = {'name': 'Видео', 'dir_name': 'video',
          'ext': movies_ext, 'sort': True, 'files': []}
documents = {'name': 'Документы', 'dir_name': 'documents',
             'ext': documents_ext, 'sort': True, 'files': []}
music = {'name': 'Музыка', 'dir_name': 'audio',
         'ext': music_ext, 'sort': True, 'files': []}
archives = {'name': 'Архиы', 'dir_name': 'archives',
            'ext': archives_ext, 'sort': True, 'files': []}
unknown = {'name': 'Другое', 'dir_name': 'other',
           'ext': [], 'sort': False, 'files': [], 'dirs': []}
extensions_list = {'known': [], 'unknown': []}
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


def get_os_objs(path, ext='*', show_all_files_dirs=typeObj.ALL, categories_list=[]):
    if not isinstance(path, (PosixPath, WindowsPath)):
        print('ERROR:', 'path must be a PosixPath or WindowsPath')
        return False
    try:
        if show_all_files_dirs in [typeObj.ALL, typeObj.DIRS] and path.is_dir():
            yield (typeObj.DIRS, path)
        for sys_obj in path.iterdir():
            if sys_obj.is_dir():
                # если имя каталога не в списке категорий
                if sys_obj.name not in categories_list:
                    # если каталог пустой нужно его удалить
                    if not list(Path(sys_obj).iterdir()):
                        try:
                            Path(sys_obj).rmdir()
                            parent_dir = sys_obj.parent
                            if not list(Path(parent_dir).iterdir()):
                                Path(parent_dir).rmdir()
                        except OSError:
                            print('WARNING:',
                                  f'The {sys_obj} directory is not empty')
                    else:
                        sys_obj = sys_obj.rename(
                            sys_obj.with_name(normalize(sys_obj.name)))
                        yield from get_os_objs(sys_obj, ext=ext, show_all_files_dirs=show_all_files_dirs, categories_list=categories_list)
            else:
                sys_obj = sys_obj.rename(
                    str(sys_obj.with_name(normalize(sys_obj.stem)))+sys_obj.suffix)
                if sys_obj.match('**'+ext) and show_all_files_dirs in [typeObj.ALL, typeObj.FILES]:
                    yield (typeObj.FILES, sys_obj)
    except FileNotFoundError as e:
        if e.errno == 2:
            print('ERROR:', 'No such file or directory')


try:
    # AHTUNG: если ругается на ошибку WinError 122 это значит в пути указаны не те слеши. Нужно "/"
    _dir = Path(argv[1])
except IndexError:
    print("Fatal error: Use the target directory path parameter to run the program.")
    exit()
except Exception as err:
    print(f"Fatal error: {str(err)}")
    exit()

# список категорий, которые подлежат сортировке
cat_dirs = [cat['dir_name'] for cat in categories if cat['sort'] == True]
# создаем подкаталоги для категорий в целевом каталоге
for cat in cat_dirs:
    _dir.joinpath(cat).mkdir(parents=True, exist_ok=True)

# генерируем список файлов, содержащихся в целевом каталоге
gen = get_os_objs(_dir, show_all_files_dirs=typeObj.FILES,
                  categories_list=cat_dirs)

for type_obj, path_name in gen:
    if type_obj == typeObj.FILES:
        name_ext, ext = path_name.name, path_name.suffix[1:]
        for cat in [c for c in categories if c['sort'] == True]:
            know_ext = False
            if ext in cat['ext']:
                cat['files'].append(name_ext)
                # move the files to the directory of the selected category
                out_file = _dir.joinpath(cat['dir_name'], name_ext)
                end_name = out_file.stem+datetime.now().strftime('_%d%m%Y_%H%M%S_') + \
                    str(randint(1, 10000))
                if ext in archives_ext:
                    out_file = _dir.joinpath(cat['dir_name'], end_name)
                    unpack_archive(path_name, out_file)
                    path_name.unlink()
                else:
                    if out_file.exists():
                        out_file = _dir.joinpath(
                            cat['dir_name'], end_name+out_file.suffix)
                    path_name.replace(out_file)
                know_ext = True
                break
        if know_ext:
            if ext not in extensions_list['known']:
                extensions_list['known'].append(ext)
        else:
            if ext not in extensions_list['unknown']:
                extensions_list['unknown'].append(ext)

# удаляем пустые каталоги в целевом каталоге (кроме каталогов для категорий)
for f in _dir.rglob('*'):
    if f.is_dir():
        if not list(f.iterdir()) and f.name not in cat_dirs:
            f.rmdir()


print(f"В каталоге \n{_dir}\nимеются следующие файлы:")
for cat in [c for c in categories if c['sort'] == True]:
    print(f"{cat['name']:<12}: {', '.join(cat['files'])}")
# print(f"{'Каталоги':<12}: {', '.join(unknown['dirs'])}")
print('Список известных расширений:', ', '.join(extensions_list['known']))
print('Список неизвестных расширений:', ', '.join(extensions_list['unknown']))
