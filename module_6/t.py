from pathlib import Path
from sys import argv

_dir = Path(r"d:/1.КУРСЫ_goIT/ДЗ/Tech Skills/goit-python/1.EMPTY_/")


# def del_dir(path, cat_lst):
#     for f in path.rglob('*'):
#         if f.is_dir() and f.name not in cat_lst:
#             if not list(f.iterdir()):


# def walk(path):
#     for p in Path(path).iterdir():
#         if p.is_dir():
#             yield from walk(p)
#             continue
#         yield p.resolve()


# for s in walk(p):
#     print(s)

def del_dir(path):
    print('test')
    for f in path.rglob('*'):
        print(f)
        if f.is_dir():
            print(f)
            if not list(f.iterdir()):  # and f.name not in cat_dirs:
                f.rmdir()
                yield from del_dir(path)
                print(f)


del_dir(_dir)
