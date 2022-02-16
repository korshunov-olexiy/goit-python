from random import randint
from datetime import datetime

def datetime_generator():
    for day in range(1,31):
        for hm in ["08:00", "09:10", "10:05", "11:15", "12:00", "15:20", "16:10", "17:05", "18:00"]:
            dt = datetime.now().date().replace(year=2001, month=7, day=day).strftime("%d.%m.%Y")
            yield datetime.strptime(f"{dt} {hm}", "%d.%m.%Y %H:%M")

datetimes = datetime_generator()
groups = lambda: randint(1,3)
subjects = lambda: randint(1,5)
teachers = lambda: randint(1,3)
grades = lambda: randint(1,5)

students = (("Карина", "Ведмидера", "k.vedmedera@gmail.com", "+38066-345-12-23", 2),
("Валентина", "Немеш", "v.nemesh@gmail.com", "+38050-864-21-32", 2),
("Анна", "Науменко", "a.naumenko@gmail.com", "+38067-484-13-21", 2),
("Софія", "Малус", "s.malus@gmail.com", "+38097-344-50-56", 2),
("Альона", "Павленко", "a.pavlenko@gmail.com", "+38050-112-32-18", 2),
("Владіслав", "Харченко", "v.harchenko@gmail.com", "+38050-211-22-81", 1),
("Іван", "Воробйов", "i.vorobiyoff@gmail.com", "+38050-121-45-71", 1),
("Катерина", "Шамкало", "k.shamkalo@gmail.com", "+38066-331-67-99", 2),
("Віталій", "Козловський", "v.kozlovsky@gmail.com", "+38066-456-54-66", 1),
("Юлія", "Розгон", "j.rozgon@gmail.com", "+38066-555-66-12", 2),
("Тетяна", "Головач", "t.golovach@gmail.com", "+38050-551-16-21", 2),
("Артем", "Мірошниченко", "a.miroshnichenko@gmail.com", "+38066-888-56-87", 1),
("Євгенія", "Бондаренко", "e.bondarenko@gmail.com", "+38050-155-62-78", 2),
("Анастасія", "Тутук", "a.tutuk@gmail.com", "+38066-900-08-35", 2),
("Іван", "Челноков", "i.chelnokov@gmail.com", "+38068-454-77-34", 1),
("Маргарита", "Голубнича", "m.golubcha@gmail.com", "+38050-090-80-53", 2),
("Григорій", "Пивоваров", "g.pivovaroff@gmail.com", "+38066-441-67-54", 1),
("Андрій", "Носенко", "a.nosenko@gmail.com", "+38066-232-11-04", 1),
("Катерина", "Логвиненко", "k.logvinenko@gmail.com", "+38050-231-67-99", 2),
("Владислава", "Матьякубова", "v.matijakubova@gmail.com", "+38050-132-33-99", 2),
("Яна", "Євдокімова", "j.evdokimova@gmail.com", "+38067-144-33-99", 2),
("Максим", "Дудко", "m.dudko@gmail.com", "+38050-777-11-04", 1),
("Артур", "Гуденко", "a.gudenko@gmail.com", "+38067-666-22-04", 1),
("Владислав", "Колос", "v.kolos@gmail.com", "+38067-555-22-04", 1),
("Богдан", "Ващенко", "b.vaschenko@gmail.com", "+38068-444-22-04", 1),
("Руслан", "Вербицький", "r.verbitsky@gmail.com", "+38067-333-22-04", 1),
("Ілля", "Дейнека", "i.deyneka@gmail.com", "+38067-222-22-04", 1),
("Артем", "Юрченко", "a.yurchenko@gmail.com", "+38067-111-22-04", 1),
("Вікторія", "Сокура", "v.sokura@gmail.com", "+38055-114-33-99", 2),
("Владислав", "Трофименко", "v.trofimenko@gmail.com", "+38066-341-22-04", 1))

# == СОЗДАЕМ ДАННЫЕ ДЛЯ ТАБЛИЦЫ "students" ==
print("INSERT INTO students (first_name, last_name, email, phone, teacher_id, subject_id, group_id, value) VALUES")
for student in students:
    for j in range(0,20):
        subject = subjects()
        st = ', '.join(map(lambda s: f"\"{str(s)}\"" if isinstance(s, str) else s, student))
        print(f"{st}, {teachers()}, {subject}, {groups()}, {grades()})", end=", ")

# == СОЗДАЕМ ДАННЫЕ ДЛЯ ТАБЛИЦЫ "grades" ==
# print("INSERT INTO grades (student_id, teacher_id, subject_id, value) VALUES")
# for student in range(1,31):
#     for j in range(0,20):
#         subject = subjects()
#         print(f"({student}, {teachers()}, {subject}, {grades()})", end=", ")

# print("INSERT INTO lessons (teacher_id, group_id, subject_id) VALUES")
# for dt_hm in datetimes:
#     print(f"({teachers()}, {groups()}, {subjects()}, \"{dt_hm}\")", end=", ")

# s = 1
# print(f"INSERT INTO groups (name, student_id) VALUES")
# for group in ["І-12", "ІМз-01с", "ІК.мз-11с"]:
#     for student in range(s, s+10):
#         print(f"(\"{group}\", {student})", end=", ")
#     s = s+10
