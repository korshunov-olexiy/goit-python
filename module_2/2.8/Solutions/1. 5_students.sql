-- 5 студентов с наибольшим средним баллом по всем предметам.
-- example: https://site-do.ru/db/sql6.php

select students.last_name as 'last name', students.first_name as 'first name', email, phone, genders.name as sex, AVG(value) as avg_grade
  from grades, students, genders
    WHERE grades.student_id = students.student_id and students.gender_id = genders.gender_id
    group by grades.student_id ORDER BY avg_grade DESC LIMIT 5;
