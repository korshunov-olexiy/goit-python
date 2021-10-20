from pathlib import Path

p = Path.cwd().joinpath('cats.txt')


def get_cats_info(path):
    res = []
    with open(path, 'r') as fn:
        lines = fn.read().splitlines()
    for l in lines:
        l = l.split(',')
        res.append({'id': l[0], 'name': l[1], 'age': l[2]})
    return res


print(get_cats_info(p))
