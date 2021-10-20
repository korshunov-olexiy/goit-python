'''
рекурсивная функция, которая превращает
этот список ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
в этот ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
'''


def encode(data):
    if data == []:
        return data
    cnt = 0
    for d in data:
        if d == data[0]:
            cnt += 1
        else:
            break
    return [data[0], cnt] + encode(data[cnt:])


lst = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
print(encode(lst))
