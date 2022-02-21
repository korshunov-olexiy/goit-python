from random import randint
from typing import List
from datetime import datetime, timedelta


def get_sql(vals):
    vals = ', '.join(vals).replace("VALUES,", "VALUES")
    return f"{vals};"

phones = lambda: randint(100000000, 900000000)

data_for_sql = ["students.txt", "teachers.txt"]

def load_data(f_name: str, is_row: bool = True) -> List:
    with open(f_name, "r", encoding="utf8") as f:
        return f.read().splitlines() if is_row else [student.split(",") for student in f.read().splitlines()]

def load_data2(f_name: str) -> List:
    with open(f_name, "r", encoding="utf8") as f:
        return f.read().strip().split(",")

departments = load_data("departments.txt", True)
groups = load_data("groups.txt", False)

students = [data for data in load_data("students.txt", False)]
teachers = load_data2("teachers.txt")
subjects = load_data2("subjects.txt")

len_departments = len(departments)
len_groups = sum([len(gr) for gr in groups])
len_students = sum([len(st) for st in students])
len_teachers = len(teachers)
len_subjects = len(subjects)

rand_obj = lambda ln: randint(1, ln)

groups_students = ["INSERT INTO groups_students (group_id, student_id) VALUES"]
sql_lessons = ["INSERT INTO lessons (subject_id, student_id, teacher_id, grade, created_at) VALUES"]
sql_departaments = ["INSERT INTO departments (name) VALUES"]
sql_groups = ["INSERT INTO groups (name, department_id) VALUES"]
sql_students = ["INSERT INTO students (last_name, first_name, email, phone, gender_id, group_id) VALUES"]
sql_teachers = ["INSERT INTO teachers (last_name, first_name, email, phone, gender_id) VALUES"]

idx_student = 1
for index, department in enumerate(departments, start=1):
    sql_departaments.append(f"(\"{department}\")")
    for group in groups[index-1]:
        sql_groups.append(f"(\"{group}\", {index})")
    for student in students[index-1]:
        last_name, first_name, email, gender = student.split()
        sql_students.append(f"(\"{last_name}\", \"{first_name}\", \"{email}\", \"{phones()}\", {gender}, {rand_obj(len_groups)})")
        idx_student += 1

for idx_student in range(1, len_students+1):
    groups_students.append(f"({rand_obj(len_groups)}, {idx_student})")

for teacher in teachers:
    last_name, first_name, email, gender = teacher.split()
    sql_teachers.append(f"(\"{last_name}\", \"{first_name}\", \"{email}\", \"{phones()}\", {gender})")

def datetime_generator():
    dt_short_format = "%d.%m.%Y"
    start_date = datetime.strptime(f"01.03.2001", "%d.%m.%Y")
    for day in range(1,len_students//4):
        for hm in ["08:00", "09:10", "10:05", "11:15", "12:00", "15:20", "16:10", "17:05", "18:00"]:
            dt = (start_date + timedelta(days=day)).strftime(dt_short_format)
            yield datetime.strptime(f"{dt} {hm}", "%d.%m.%Y %H:%M")

datetimes = datetime_generator()

for dt_hm in datetimes:
    for lessons_count in range(1,randint(8,15)):
        sql_lessons.append(f"({rand_obj(len_subjects)}, {rand_obj(len_students)}, {rand_obj(len_teachers)}, {rand_obj(5)}, \"{dt_hm}\")")

# === OUTPUT DATA:
departments = get_sql(sql_departaments)
groups = get_sql(sql_groups)
subjects = "INSERT INTO subjects (name) VALUES " + ', '.join([f"(\"{sub}\")" for sub in subjects]) + ";"
students = get_sql(sql_students)
teachers = get_sql(sql_teachers)
groups_students = get_sql(groups_students)
lessons = get_sql(sql_lessons)

print(students)
