from typing import List


data_for_sql = ["students.txt", "teachers.txt"]

def load_data(f_name: str, is_row: bool = True) -> List:
    with open(f_name, "r", encoding="utf8") as f:
        return f.read().splitlines() if is_row else [student.split(",") for student in f.read().splitlines()]

def load_data2(f_name: str) -> List:
    with open("groups.txt", "r", encoding="utf8") as f:
        return f.read().strip().split(",")

departments = load_data("departments.txt", True)
groups = load_data("groups.txt", False)
students = load_data("students.txt", False)


sql_departaments = ["INSERT INTO departments (name) VALUES"]
sql_groups = ["INSERT INTO groups (name, department_id) VALUES"]
sql_students = ["INSERT INTO students (last_name, first_name, email, phone) VALUES"]
for index, department in enumerate(departments, start=1):
    sql_departaments.append(f"(\"{department}\")")
    for group in groups[index-1]:
        sql_groups.append(f"(\"{group}\", {index})")
    for student in students[index-1]:
        last_name, first_name = student.split()
        sql_students.append(f"(\"{last_name}\", \"{first_name}\", {index})")

departments = ', '.join(sql_departaments).replace("VALUES,", "VALUES") + ";"
groups = ', '.join(sql_groups).replace("VALUES,", "VALUES") + ";"
students = ', '.join(sql_students).replace("VALUES,", "VALUES") + ";"
print(f"{students}")
