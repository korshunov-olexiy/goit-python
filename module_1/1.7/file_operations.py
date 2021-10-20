'''
Реализуйте функцию file_operations(path, additional_info, start_pos, count_chars),
которая добавляет дополнительную информацию в файл по пути path из параметра additional_info
и после этого возвращает строку с позиции start_pos длиной count_chars
'''


def standard_input():
    yield "file_operation.txt"


def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as fw:
        fw.write(f"{additional_info}\n")
    with open(path, 'r') as fr:
        fr.seek(start_pos)
        ln = fr.read()[:count_chars]
    return ln


print(file_operations(input(), "additional info", 3, 6))
