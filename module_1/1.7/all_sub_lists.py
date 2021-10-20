# отобрать все варианты списка
def all_sub_lists(data):
    res = []
    for i in range(len(data)):
        for j in range(i+1, len(data)+1):
            res.append(data[i:j])
    res.insert(0, [])
    return sorted(res, key=len)


# lst = [1, 2, 3]
# result: [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
lst = [0, 1, 1, 2, 4, 5, 8]
# result: [[], [0], [1], [1], [2], [0, 1], [1, 1], [1, 2], [0, 1, 1], [1, 1, 2], [0, 1, 1, 2]]
print(all_sub_lists(lst))
