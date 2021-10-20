from pathlib import Path

p = Path.cwd().joinpath('sotr.txt')


def read_employees_from_file(path):
    lst = []
    fn = open(path, 'r')
    while True:
        line = fn.readline()
        if not line:
            break
        else:
            lst.append(line.strip())
    fn.close()
    return lst


print(read_employees_from_file(p))
