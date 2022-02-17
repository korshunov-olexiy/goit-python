def load_data(f_name: str):
    with open("students.txt", "r", encoding="utf8") as f:
        data = [student.split(",") for student in f.read().splitlines()]
    result = list(map(lambda st: list(map(lambda s: s.split(), st)), data))

for group in students:
    for last_name, first_name in group:
        print(last_name, first_name)
    print("")
