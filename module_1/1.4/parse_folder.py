import sys
from pathlib import Path


def parse_folder(path):
    files = []
    folders = []
    p = Path(path).parent
    iterator = p.iterdir()
    for sys_obj in iterator:
        if sys_obj.is_dir():
            folders.append(sys_obj.name)
        else:
            files.append(sys_obj.name)
    return files, folders

print( parse_folder(Path(sys.argv[0])) )
