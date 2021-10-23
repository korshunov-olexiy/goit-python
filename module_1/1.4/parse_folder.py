from pathlib import Path


def parse_folder(path):
    files = []
    folders = []
    p = Path(path)
    iterator = p.iterdir()
    for i in iterator:
        if i.is_dir():
            folders.append(i.name)
        else:
            files.append(i.name)
    return files, folders

print( parse_folder("./path") )
