from datetime import datetime
from pathlib import Path, PosixPath, WindowsPath
from sys import argv
from shutil import unpack_archive
from random import randint
import re

try:
    # AHTUNG: если ругается на ошибку WinError 122 это значит в пути указаны не те слеши. Нужно "/"
    _dir = Path(argv[1])
except IndexError:
    print("Fatal error: Use the target directory path parameter to run the program.")
    exit()
except Exception as err:
    print(f"Fatal error: {str(err)}")
    exit()

pictures_ext = ['bmp', 'jpeg', 'png', 'jpg', 'gif']
movies_ext = ['avi', 'mp4', 'mov']
documents_ext = ['pdf', 'doc', 'docx', 'txt']
music_ext = ['mp3', 'ogg', 'wav', 'amr']
archives_ext = ['zip', 'gz', 'tar']

# словари для каждой категории. ключ 'tag' используется в функциях обработки файлов (move_media, move_archives)
pictures = {'name': 'Изображения', 'dir_name': 'images', 'ext': pictures_ext, 'sort': True, 'tag': 'media', 'files': []}
movies = {'name': 'Видео', 'dir_name': 'video', 'ext': movies_ext, 'sort': True, 'tag': 'media', 'files': []}
documents = {'name': 'Документы', 'dir_name': 'documents', 'ext': documents_ext, 'sort': True, 'tag': 'media', 'files': []}
music = {'name': 'Музыка', 'dir_name': 'audio', 'ext': music_ext, 'sort': True, 'tag': 'media', 'files': []}
archives = {'name': 'Архиы', 'dir_name': 'archives', 'ext': archives_ext, 'sort': True, 'tag': 'archive', 'files': []}
unknown = {'name': 'Другое', 'dir_name': 'other', 'ext': [], 'sort': False, 'tag': 'other', 'files': [], 'dirs': []}
extensions_list = {'known': [], 'unknown': []}
categories = [pictures, movies, documents, music, archives, unknown]

# декоратор для констант типов файлов
def constant(f):
    def fset(self, value): raise TypeError
    def fget(self): return f()
    return property(fget, fset)

# классы для выбора констант 'all', 'files', 'dirs'
class TypeOfShowObject(object):
    @constant
    def ALL(): return 'all'
    @constant
    def FILES(): return 'files'
    @constant
    def DIRS(): return 'dirs'

typeObj = TypeOfShowObject()

table_symbols = ('абвгґдеєжзиіїйклмнопрстуфхцчшщюяыэАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЮЯЫЭьъЬЪ',
                 (*(u'abvhgde'), 'ye', 'zh', *(u'zyi'), 'yi', *(u'yklmnoprstuf'), 'kh', 'ts', 'ch', 'sh', 'shch', 'yu', 'ya', 'y', 'ye', *(u'ABVHGDE'), 'Ye', 'Zh', *(u'ZYI'), 'Yi', *(u'YKLMNOPRSTUF'), 'KH', 'TS', 'CH', 'SH', 'SHCH', 'YU', 'YA', 'Y', 'YE', *(u'_'*4)))
map_cyr_to_latin = {ord(src): dest for src, dest in zip(*table_symbols)}

def del_empty_dirs(path, sort_dirs):
    """Рекурсивное удаление пустых каталогов в целевом каталоге path.
    
    Ключевые аргументы:
    path -- каталог, в котором будет проводиться удаление
    sort_dirs -- список имен каталогов, которые будут пропущены в любом случае
    """
    for f in path.rglob('*'):
        if f.is_dir():
            if not list(f.iterdir()) and f.name not in sort_dirs:
                f.rmdir()
                return del_empty_dirs(path, sort_dirs)


def move_archives(root_dir, file_name):
    """Распаковка архива в каталог root_dir с последующим удалением исходного архива
    
    Ключевые аргументы:
    root_dir -- каталог, в который будет распаковываться архив
    file_name -- имя архива
    """
    if root_dir.joinpath(file_name.stem).exists():
        unpack_archive(path_name, root_dir.joinpath(f"{file_name.stem}_{str(datetime.now().microsecond)}"))
    else:
        unpack_archive(path_name, root_dir.joinpath(f"{file_name.stem}"))
    # удаляем исходный архив file_name
    file_name.unlink()


def move_media(root_dir, file_name):
    """Перенос файла по тэгу 'media' в каталог root_dir
    
    Ключевые аргументы:
    root_dir -- каталог, в который будет распаковываться архив
    file_name -- имя исходного файла
    """
    if root_dir.joinpath(file_name.name).exists():
        file_name.replace(root_dir.joinpath(f"{file_name.stem}_{str(datetime.now().microsecond)}{file_name.suffix}"))
    else:
        file_name.replace(root_dir.joinpath(file_name.name))


def normalize(in_str):
    """Замена НЕ ЛАТИНСКИХ символов И ЦИФР в переданной строке на латинские и '_'
    
    Ключевые аргументы:
    in_str -- строка, которая будет подвергнута изменению
    """
    global table_symbols, map_cyr_to_latin
    rx = re.compile(r"[^\w_]")
    return rx.sub('_', in_str.translate(map_cyr_to_latin))


def sort_dir(path, ext='*', show_all_files_dirs=typeObj.ALL, categories_list=[]):
    """Рекусривно ищем в переданном каталоге файлы/каталоги или файлы или каталоги,
    пропуская каталоги из переданной категории.

    Ключевые аргументы:
    path -- целевой каталог, в котором ищем объекты
    ext -- расширение файлов, которые попадут в вывод (без точек)
    show_all_files_dirs -- какие объекты выдавать в выводе: ВСЕ, ФАЙЛЫ или КАТАЛОГИ
    categories_list -- список каталогов, в которых не будет проводиться поиск
    """
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
                    sys_obj = sys_obj.rename(sys_obj.with_name(normalize(sys_obj.name)))
                    yield from sort_dir(sys_obj, ext=ext, show_all_files_dirs=show_all_files_dirs, categories_list=categories_list)
            else:
                sys_obj = sys_obj.rename(
                    str(sys_obj.with_name(normalize(sys_obj.stem)))+sys_obj.suffix)
                if sys_obj.match('**'+ext) and show_all_files_dirs in [typeObj.ALL, typeObj.FILES]:
                    yield (typeObj.FILES, sys_obj)
    except FileNotFoundError as e:
        if e.errno == 2:
            print('ERROR:', 'No such file or directory')


# словарь: имя_каталога и список расширений категории
cat_dirs = {cat['dir_name']: cat['ext'] for cat in categories}

for cat in cat_dirs.keys():
    # Создаем подкаталоги для категорий в целевом каталоге
    _dir.joinpath(cat).mkdir(parents=True, exist_ok=True)

# генерируем список файлов, содержащихся в целевом каталоге
gen = sort_dir(_dir, show_all_files_dirs=typeObj.FILES, categories_list=cat_dirs.keys())

# сортируем файлы: с тэгом media и archive по своим правилам
for type_obj, path_name in gen:
    if type_obj == typeObj.FILES:
        name_ext, ext = path_name.name, path_name.suffix[1:]
        # по расширению файла path_name определяем имя каталога, в который будем перемещать файлы
        cat_dir = ''.join([k for k,v in cat_dirs.items() if ext in v])
        # добавляем найденные имена файлов в список файлов для определенной категории
        [cat['files'].append(name_ext) for cat in categories if cat['dir_name'] == cat_dir]
        # если расширение файла в списке расширений
        # (а значит вычисленное имя каталога для расширений != '')
        if cat_dir:
            # если это файл из тэга 'media' (док-т, музыка, видео, изображение)
            if ext in [c for cat in categories for c in cat['ext'] if cat['tag'] == 'media']:
                move_media(_dir.joinpath(cat_dir), path_name)
            # если это архив (тэг 'archive')
            elif ext in [c for cat in categories for c in cat['ext'] if cat['tag'] == 'archive']:
                move_archives(_dir.joinpath(cat_dir), path_name)
            # добавляем расширение файла в список известных расширений
            if ext not in extensions_list['known']:
                extensions_list['known'].append(ext)
        # если нашли файл с неизвестным расширением
        else:
            # добавляем расширение файла в список не известных расширений
            if ext not in extensions_list['unknown']:
                extensions_list['unknown'].append(ext)

# удаляем пустые каталоги в целевом каталоге (кроме каталогов для категорий)
del_empty_dirs(_dir, cat_dirs)

# Выдаем результат работы программы в форматированном виде
print(f"В каталоге \n{_dir}\nимеются следующие файлы:")
for cat in [c for c in categories if c['sort'] == True]:
    print(f"{cat['name']:<12}: {', '.join(cat['files'])}")
# print(f"{'Каталоги':<12}: {', '.join(unknown['dirs'])}")
print('Список известных расширений:', ', '.join(extensions_list['known']))
print('Список неизвестных расширений:', ', '.join(extensions_list['unknown']))
