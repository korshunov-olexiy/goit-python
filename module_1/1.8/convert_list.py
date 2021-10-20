import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    func_cat = []
    if isinstance(cats[0], Cat):
        for cat in cats:
            func_cat.append({'nickname': cat.nickname,
                            'age': cat.age, 'owner': cat.owner})
    else:
        for cat in cats:
            func_cat.append(Cat(cat['nickname'], cat['age'], cat['owner']))
    return func_cat


# lst = [Cat(nickname='Mick', age=5, owner='Sara'),
#        Cat(nickname='Barsik', age=7, owner='Olga'),
#        Cat(nickname='Simon', age=3, owner='Yura')]

lst = [{'nickname': 'Mick', 'age': 5, 'owner': 'Sara'},
       {'nickname': 'Barsik', 'age': 7, 'owner': 'Olga'},
       {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}]

print(convert_list(lst))
