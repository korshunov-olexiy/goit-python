from pathlib import Path, PosixPath, WindowsPath
# from string import ascii_letters
import re


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


def get_files_recur(path, ext='*', show_all_files_dirs=typeObj.ALL):
    if not isinstance(path, (PosixPath, WindowsPath)):
        print('ERROR:', 'path must be a PosixPath or WindowsPath')
    try:
        if show_all_files_dirs in [typeObj.ALL, typeObj.DIRS] and path.is_dir():
            yield ('dir', path)
        for sys_obj in path.iterdir():
            if sys_obj.is_dir():
                path = Path(Path.rename(sys_obj, Path.joinpath(
                    sys_obj.parent, normalize(sys_obj.name))))
                yield from get_files_recur(path, ext=ext, show_all_files_dirs=show_all_files_dirs)
            else:
                name, extension = sys_obj.stem, sys_obj.suffix
                path = Path(Path.rename(sys_obj, Path.joinpath(
                    sys_obj.parent, normalize(name)+extension)))
                if sys_obj.match('**'+ext) and show_all_files_dirs in [typeObj.ALL, typeObj.FILES]:
                    yield ('file', sys_obj)
    except FileNotFoundError as e:
        if e.errno == 2:
            print('ERROR:', 'No such file or directory')


_dir = Path(r"/home/user1/1. COURSES/goit/ДЗ/Tech Skills/3/1.test_")
gen = get_files_recur(_dir)
for g in gen:
    g
