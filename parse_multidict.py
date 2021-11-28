from typing import List
from itertools import islice

mydict = {'Неклеточные': {'Вирусы': 100, 'Фаги': 20},
        'Клеточные':
            {'Прокариоты':
                {'Бактерии': 576,'Архебактерии': 590},
                'Эукариоты':
                {
                    'Растения': 788,
                    'Животные':{'Одноклеточные': 257,'Многоклеточные': 358},
                    'Грибы': 256,
                    'Лишайники': 73
                }
            }
        }

def direct_dict(d: dict) -> List:
    for key, item in d.items():
        if isinstance(item, str):
            #print(item)
            return list({key: item})
        else:
            #print(item)
            for k,i in item.items():
                    
                return direct_dict(dict(list(d.items())[1:]))


def decode(data):
    if data == []:
        return data
    if isinstance(data[1], int):
        return list(data[0]*data[1]) + decode(data[2:])
    else:
        return decode(data[2:])

# for key, item in mydict.items():
#     if isinstance(item, str):
#         print(key, item)
#     for k,i in item.items():
#         if isinstance(i, dict):
#             print(k, i.items())
#             for k1,i1 in item.items():
#                 if isinstance(i1, dict):
#                     print(k1, i1)

print(direct_dict(mydict))
