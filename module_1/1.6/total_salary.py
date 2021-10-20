from pathlib import Path


def total_salary(path):
    sm = 0
    fn = open(path)
    while True:
        line = fn.readline()
        if not line:
            break
        else:
            sm += float(line.strip().split(',')[1])
    fn.close()
    return sm


p = Path.cwd().joinpath('salary.txt')
print(total_salary(p))
