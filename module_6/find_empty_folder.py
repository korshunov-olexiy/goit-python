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


def get_files_recur(path, ext='*', show_all_files_dirs=typeObj.ALL):
    if not isinstance(path, (PosixPath, WindowsPath)):
        print('ERROR:', 'path must be a PosixPath or WindowsPath')
    try:
        if show_all_files_dirs in [typeObj.ALL, typeObj.DIRS] and path.is_dir():
            yield ('dir', path)
        for sys_obj in path.iterdir():
            if sys_obj.is_dir():
                if not list(Path(sys_obj).iterdir()):
                    #print("empty folder: ", sys_obj)
                    print( sys_obj )
                yield from get_files_recur(sys_obj, ext=ext, show_all_files_dirs=show_all_files_dirs)
            else:
                if sys_obj.match('**'+ext) and show_all_files_dirs in [typeObj.ALL, typeObj.FILES]:
                    yield ('file', sys_obj)
    except FileNotFoundError as e:
        if e.errno == 2:
            print('ERROR:', 'No such file or directory')


_dir = Path(r"/home/user1/1. COURSES/goit_github/1.test_")
gen = get_files_recur(_dir)
for g in gen:
    g
