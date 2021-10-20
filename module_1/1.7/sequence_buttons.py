'''
Напишите функцию sequence_buttons, отображающую последовательность кнопок,
которую необходимо нажать, чтобы на экране телефона появился текст, введенный пользователем.
Создайте словарь, сопоставляющий символы с кнопками, которые необходимо нажать.
Пример, если функции sequence_buttons передать строку "Hello, World!"
функция должна вернуть "4433555555666110966677755531111".
Требования:
    функция корректно обрабатывает строчные и прописные буквы.
    функция игнорирует символы, не входящие в указанный перечень
'''


def sequence_buttons(string):
    symbols = (' .,?!:abcdefghijklmnopqrstuvwxyz')
    string = ''.join(filter(lambda s: s in symbols, string.lower()))
    map_chars = {}
    for l in symbols:
        if l in '.,?!:':
            btn, cnt = 1, '.,?!:'.index(l)+1
        elif l in 'abc':
            btn, cnt = 2, 'abc'.index(l)+1
        elif l in 'def':
            btn, cnt = 3, 'def'.index(l)+1
        elif l in 'ghi':
            btn, cnt = 4, 'ghi'.index(l)+1
        elif l in 'jkl':
            btn, cnt = 5, 'jkl'.index(l)+1
        elif l in 'mno':
            btn, cnt = 6, 'mno'.index(l)+1
        elif l in 'pqrs':
            btn, cnt = 7, 'pqrs'.index(l)+1
        elif l in 'tuv':
            btn, cnt = 8, 'tuv'.index(l)+1
        elif l in 'wxyz':
            btn, cnt = 9, 'wxyz'.index(l)+1
        elif l == ' ':
            btn, cnt = 0, 1
        map_chars[ord(l)] = str(btn)*cnt
    return string.translate(map_chars)


print(sequence_buttons("Hello world!"))
