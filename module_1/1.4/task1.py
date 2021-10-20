def format_ingredients(items):
    if len(items) == 0:
        return ''
    if len(items) == 1:
        return items[0]
    return ', '.join(items[:-1]) + ' и ' + items[-1]


print(format_ingredients([]))
print(format_ingredients(['уксус 1 л.', 'батон']))
print(format_ingredients(['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус']))


def f_i(i):
    ingr = len(i)
    if ingr == 0:
        return ''.join(i)
    elif ingr == 1:
        return ''.join(i)
    else:
        l_p = i.pop(-1)
        f_p = ', '.join(i)
        r = f_p + ' и ' + l_p
    return r


print(f_i(['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус']))
