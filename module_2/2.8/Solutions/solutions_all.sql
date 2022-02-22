-- 5 студентов с наибольшим средним баллом по всем предметам
select students.student_id, students.last_name, students.first_name, round(avg(grade),3) as avg_grade from students, lessons
where students.student_id = lessons.student_id
group by lessons.student_id order by avg_grade DESC LIMIT 5;

-- 1 студент с наивысшим средним баллом по одному предмету
select students.student_id, students.last_name, students.first_name, round(avg(grade),3) as avg_grade from students, lessons
where students.student_id = lessons.student_id
group by lessons.subject_id order by avg_grade DESC LIMIT 1;

-- средний балл в группе по одному предмету
select s1.group_name, s1.subject_name, round(avg(grade), 3) avg_grade from (select gr.name group_name, sb.name subject_name, l.grade from lessons l
inner join subjects sb
inner join students s
inner join groups gr
on s.group_id = gr.group_id and l.student_id = s.student_id and sb.subject_id = l.subject_id) s1
group by s1.subject_name, s1.group_name order by s1.group_name;


-- Средний балл в потоке (что такое поток)??
select sb.name, round(avg(grade),3) as avg_grade from lessons l, subjects sb
where sb.subject_id = l.subject_id
group by l.subject_id order by avg_grade DESC;
