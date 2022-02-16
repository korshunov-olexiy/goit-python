from random import randint


grades = lambda: randint(1,5)
subjects = lambda: randint(1,5)
teachers = lambda: randint(1,3)

print(f"INSERT INTO grades (student_id, teacher_id, subject_id, value) VALUES")
for student in range(1,31):
    for j in range(0,20):
        subject = subjects()
        print(f"({student}, {teachers()}, {subject}, {grades()})", end=", ")
