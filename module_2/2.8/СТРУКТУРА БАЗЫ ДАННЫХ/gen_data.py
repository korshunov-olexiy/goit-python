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

for index, department in enumerate(departments):
    print(department, groups[index], students[index])
