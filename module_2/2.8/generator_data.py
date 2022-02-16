from random import randint

grades = lambda: randint(1,5)
subjects = lambda: randint(1,5)

for student in range(1,31):
    for j in range(0,20):
        subject = subjects()
        print(f"INSERT INTO students_subjects (students_id, subjects_id) VALUES ({student}, {subject});")
        print(f"INSERT INTO subjects_grades (subjects_id, grades_id) VALUES ({student}, {grades()});")
