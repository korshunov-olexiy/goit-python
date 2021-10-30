'''
Напишите рекурсивную функцию decode которая раскодирует список
["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
в ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
'''


def decode(data):
    if data == []:
        return data
    if isinstance(data[1], int):
        return list(data[0]*data[1]) + decode(data[2:])
    else:
        return decode(data[2:])


lst = ['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]
print(decode(lst))
