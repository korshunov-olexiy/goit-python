import re

'''Используя генератор множеств, дополните приведенный код,
так чтобы получить множество, содержащее уникальные слова
(в нижнем регистре) строки sentence. Результат вывести на
одной строке в алфавитном порядке, разделяя элементы
одним символом пробела.'''

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
rx = re.compile(r'[\,\.\(\)\:\;]')
#print(' '.join(sorted({rx.sub('', s.lower()) for s in sentence.split()})))


'''Используя генератор множеств, дополните приведенный код,
так чтобы получить множество, содержащее уникальные слова
строки sentence длиною меньше 4 символов. Результат вывести
на одной строке (в нижнем регистре) в алфавитном порядке,
разделяя элементы одним символом пробела.'''

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
sentence = rx.sub('', sentence)
# print(' '.join(sorted({s.lower() for s in sentence.split() if len(s) < 4})))

'''Используя генератор множеств, дополните приведенный код, так чтобы
он выбрал из списка files уникальные имена файлов c расширением .png,
независимо от регистра имен и расширений. Имена файлов вывести вместе
с расширением, все на одной строке, в нижнем регистре,
в алфавитном порядке через пробел.'''

files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
files = sorted({f.lower() for f in files if f[-3:].lower() == 'png'})
print(' '.join(files))
