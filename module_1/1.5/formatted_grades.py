grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    students_grades = []
    for student, ects in students.items():
        students_grades.append((student, (ects, str(grade[ects]))))
    for idx, info in enumerate(students_grades):
        students_grades[idx] = f"{idx+1:>4}|{info[0]:<10}|{info[1][0]:^5}|{info[1][1]:^5}"
    return students_grades


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

for el in formatted_grades(students):
    print(el)
