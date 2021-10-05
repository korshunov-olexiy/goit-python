from pathlib import Path, PosixPath, WindowsPath
# from string import ascii_letters
import re


pictures_ext = ['jpeg', 'png', 'jpg']
movies_ext = ['avi', 'mp4', 'mov']
documents_ext = ['doc', 'docx', 'txt']
music_ext = ['mp3', 'ogg', 'wav', 'amr']
archives_ext = ['zip', 'gz', 'tar']

pictures = {'name': 'Изображения', 'dir_name': 'images', 'ext': pictures_ext, 'sort': True, 'files': []}
movies = {'name': 'Видео', 'dir_name': 'video', 'ext': movies_ext, 'sort': True, 'files': []}
documents = {'name': 'Документы', 'dir_name': 'documents', 'ext': documents_ext, 'sort': True, 'files': []}
music = {'name': 'Музыка', 'dir_name': 'audio', 'ext': music_ext, 'sort': True, 'files': []}
archives = {'name': 'Архиы', 'dir_name': 'archives', 'ext': archives_ext, 'sort': True, 'files': []}
unknown = {'name': 'Другое', 'dir_name': 'other', 'ext': [], 'sort': False, 'files': [], 'dirs': []}
extensions_list = {'known': [], 'unknown': []}
categories = [pictures, movies, documents, music, archives, unknown]

def copy_file(root_dir, category, name):
    pass

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
            yield ('dirs', path)
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
                            print('WARNING:', f'The {sys_obj} directory is not empty')
                    else:
                        sys_obj = sys_obj.rename(sys_obj.with_name(normalize(sys_obj.name)))
                        yield from get_os_objs(sys_obj, ext=ext, show_all_files_dirs=show_all_files_dirs, categories_list=categories_list)
            else:
                sys_obj = sys_obj.rename(str(sys_obj.with_name(normalize(sys_obj.stem)))+sys_obj.suffix)
                if sys_obj.match('**'+ext) and show_all_files_dirs in [typeObj.ALL, typeObj.FILES]:
                    yield ('files', sys_obj)
    except FileNotFoundError as e:
        if e.errno == 2:
            print('ERROR:', 'No such file or directory')


_dir = Path(r"/home/user1/1. COURSES/goit_github/1.test_")
# список категорий, которые подлежат сортировке
cat_dirs = [cat['dir_name'] for cat in categories if cat['sort'] == True]
(Path(Path.joinpath(_dir, cat)).mkdir(parents=True, exist_ok=True) for cat in cat_dirs)
# генерируем список файлов, содержащихся в целевом каталоге
gen = get_os_objs(_dir, show_all_files_dirs=typeObj.FILES, categories_list=cat_dirs)

for type_obj, path_name in gen:
    if type_obj == typeObj.FILES:
        name_ext, ext = path_name.name, path_name.suffix[1:]
        for cat in [c for c in categories if c['sort'] == True]:
            know_ext = False
            if ext in cat['ext']:
                cat['files'].append(name_ext)
                know_ext = True
                break
        if know_ext:
            if ext not in extensions_list['known']:
                extensions_list['known'].append(ext)
        else:
            if ext not in extensions_list['unknown']:
                extensions_list['unknown'].append(ext)

print(f"В каталоге \n{_dir}\nимеются следующие файлы:")
for cat in [c for c in categories if c['sort'] == True]:
    print(f"{cat['name']:<12}: {', '.join(cat['files'])}")
print(f"{'Каталоги':<12}: {', '.join(unknown['dirs'])}")
print('Список известных расширений:', ', '.join(extensions_list['known']))
print('Список неизвестных расширений:', ', '.join(extensions_list['unknown']))
