from pathlib import Path

p = Path.cwd().joinpath('recipe.txt')


def get_recipe(path, search_id):
    with open(path, 'r') as fn:
        lines = fn.read().splitlines()
    for l in lines:
        if l[:24] == search_id:
            l = l.split(',', maxsplit=2)
            return {'id': l[0], 'name': l[1], 'ingredients': l[2].split(',')}


print(get_recipe(p, '60b90c3b13067a15887e1ae4'))
