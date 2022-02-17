from random import randint
from datetime import datetime

teachers = lambda: randint(1,3)
students = lambda: randint(1,30)
groups = lambda: randint(1,3)
subjects = lambda: randint(1,5)
grades = lambda: randint(1,5)

def datetime_generator():
    for day in range(1,31):
        for hm in ["08:00", "09:10", "10:05", "11:15", "12:00", "15:20", "16:10", "17:05", "18:00"]:
            dt = datetime.now().date().replace(year=2001, month=7, day=day).strftime("%d.%m.%Y")
            yield datetime.strptime(f"{dt} {hm}", "%d.%m.%Y %H:%M")

datetimes = datetime_generator()


print("INSERT INTO grades (value, created_at, student_id, teacher_id, subject_id) VALUES")
for dt_hm in datetimes:
    data = []
    for i in range(0,5):
        pre_data = f"({grades()}, \"{dt_hm}\", {students()}, {teachers()}, {subjects()})"
        while pre_data in data:
            pre_data = f"({grades()}, \"{dt_hm}\", {students()}, {teachers()}, {subjects()})"
        data.append(pre_data)
    print(', '.join(data), end=", ")
