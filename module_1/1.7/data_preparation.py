# вернуть отсортированный по убыванию список эл-тов
# из списка списков, в котором удалены
# 1-й и посл.элементы ЕСЛИ длина списка больше 2
def data_preparation(list_data):
    res = []
    for lst in list_data:
        if len(lst) > 2:
            lst = sorted(lst)[1:-1]
        res.extend(lst)
    return sorted(res, reverse=True)


lst_data = [[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]
print(data_preparation(lst_data))
