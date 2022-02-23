-- 5 студентов с наибольшим средним баллом по всем предметам
select students.student_id, students.last_name, students.first_name, round(avg(grade),3) as avg_grade from students, lessons
where students.student_id = lessons.student_id
group by lessons.student_id order by avg_grade DESC LIMIT 5;

-- 1 студент с наивысшим средним баллом по одному предмету
select students.student_id, students.last_name, students.first_name, round(avg(grade),3) as avg_grade from students, lessons
where students.student_id = lessons.student_id
group by lessons.subject_id order by avg_grade DESC LIMIT 1;

-- средний балл в группе по одному предмету
select gr.name group_name, sb.name subject_name, round(avg(grade),3) avg_grade from lessons l
inner join subjects sb
inner join students s
inner join groups gr
on s.group_id = gr.group_id and l.student_id = s.student_id and sb.subject_id = l.subject_id
group by subject_name, group_name order by group_name;

-- Средний балл в потоке
select s.last_name, s.first_name, round(avg(grade),3) avg_grade from lessons l
inner join subjects sb
inner join students s
on l.subject_id = sb.subject_id and l.student_id = s.student_id group by s.student_id;

-- Какие курсы читает преподаватель
select DISTINCT t.last_name, t.first_name, sb.name from lessons l
inner join subjects sb
inner join teachers t
on l.subject_id = sb.subject_id and l.teacher_id = t.teacher_id
order by t.last_name, sb.name;

-- Список студентов в группе
select gr.name, s.last_name, s.first_name from students s, groups gr
where gr.group_id = s.group_id order by gr.group_id;

-- Оценки студентов в группе по предмету
select gr.name 'Group name', s.last_name || ' ' || s.first_name 'Full Name', sb.name, l.grade from lessons l
inner join subjects sb
inner join students s
inner join groups gr
on l.subject_id = sb.subject_id and gr.group_id = s.group_id
order by gr.group_id;

-- Оценки студентов в группе по предмету на последнем занятии
select gr.name 'Group name', sb.name 'Subject', s.last_name || ' ' || s.first_name 'Full Name', l.grade, l.created_at from groups gr
inner join students s
inner join subjects sb
inner join lessons l
on l.subject_id = sb.subject_id and l.student_id = s.student_id and s.group_id = gr.group_id and l.created_at = (select max(l2.created_at) from lessons l2)
order by sb.subject_id;

-- Список курсов, которые посещает студент
select s.last_name || ' ' || s.first_name 'Subject', sb.name from students s
inner join lessons l
inner join subjects sb
on s.student_id = l.student_id and l.subject_id = sb.subject_id order by s.student_id;

-- Средний балл, который преподаватель ставит студенту
select t.last_name || ' ' || t.first_name teacher, s.last_name || ' ' || s.first_name students, round(avg(l.grade),3) avg_grade from lessons l
inner join teachers t
inner join students s
on l.student_id = s.student_id and l.teacher_id = t.teacher_id
group by l.student_id, t.teacher_id
order by t.teacher_id, s.student_id;

-- Средний балл, который ставит преподаватель
select t.last_name || ' ' || t.first_name teacher, round(avg(l.grade), 3) avg_grade from teachers t
left join lessons l
on l.teacher_id = t.teacher_id
group by teacher order by l.grade DESC;
