DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS genders;
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS lessons;
DROP table if exists students_subjects;
DROP TABLE IF EXISTS teachers_subjects;
DROP TABLE IF EXISTS groups_subjects;


CREATE TABLE students (
	student_id INTEGER PRIMARY KEY,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	email VARCHAR(30) NOT NULL,
	phone VARCHAR(30) NOT NULL,
	gender_id INTEGER,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT genders_FK FOREIGN KEY (gender_id) REFERENCES genders(gender_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE genders (
  gender_id INTEGER PRIMARY KEY,
  name VARCHAR(30),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE teachers (
  teacher_id INTEGER PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(40) NOT NULL UNIQUE,
  phone VARCHAR(30) NOT NULL UNIQUE,
  gender_id INTEGER,
  lesson_id INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT genders_FK FOREIGN KEY (gender_id) REFERENCES genders(gender_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT lesson_FK FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE subjects (
  subject_id INTEGER PRIMARY KEY,
  name VARCHAR(80),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- REAL GRADES
CREATE TABLE grades (
  id INTEGER PRIMARY KEY,
  value INTEGER,
  student_id INTEGER,
  subject_id INTEGER,
  CONSTRAINT students_FK FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT subjects_FK FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE teachers_subjects(
  id INTEGER PRIMARY KEY,
  teacher_id INTEGER,
  subject_id INTEGER,
  CONSTRAINT teachers_FK FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT subjects_FK FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE groups (
  group_id INTEGER PRIMARY KEY,
  name VARCHAR(80),
  student_id INTEGER,
  lesson_id INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT students_FK FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT lesson_FK FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE groups_subjects (
  id INTEGER PRIMARY KEY,
  group_id INTEGER,
  subject_id INTEGER,
  CONSTRAINT groups_FK FOREIGN KEY (group_id) REFERENCES groups(group_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT subjects_FK FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE lessons (
  lesson_id INTEGER PRIMARY KEY,
  teacher_id INTEGER,
  started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -- -- -- -- -- -- -- -- -- -- -- --
-- ОЦЕНКИ
INSERT INTO grades (value) VALUES (1), (2), (3), (4), (5);

-- ПОЛ (МУЖЧИНА/ЖЕНЩИНА)
INSERT INTO genders (name) VALUES("male"), ("female");

-- ГРУППЫ
INSERT INTO groups (name) VALUES("І-12"), ("ІМз-01с"), ("ІК.мз-11с");

-- ПРЕДМЕТЫ
INSERT INTO subjects (name) VALUES
   ("Технічна термодинаміка"),
   ("Основи охорони праці та БЖД"),
   ("Нормативно-правове забезпечення"),
   ("ДЗВ загальної підготовки"),
   ("Деталі машин");

-- УЧИТЕЛЯ
INSERT INTO teachers (first_name, last_name, email, phone, gender_id) VALUES
  ("Андрій", "Євдокимов","a.yevdokymov@biem.sumdu.edu.ua","+38 (0542) 33-30-98", 1),
  ("Ольга","Лукаш","o.lukash@biem.sumdu.edu.ua","+38 (0542) 33-22-24", 2),
  ("Ірина","Дегтярьова","i.dehtyarova@biem.sumdu.edu.ua","+38 (0542) 33-22-23", 2);

-- СТУДЕНТЫ
 INSERT INTO students (first_name, last_name, email, phone, gender_id) VALUES
   ("Карина", "Ведмидера", "k.vedmedera@gmail.com", "+38066-345-12-23", 2),
   ("Валентина", "Немеш", "v.nemesh@gmail.com", "+38050-864-21-32", 2),
   ("Анна", "Науменко", "a.naumenko@gmail.com", "+38067-484-13-21", 2),
   ("Софія", "Малус", "s.malus@gmail.com", "+38097-344-50-56", 2),
   ("Альона", "Павленко", "a.pavlenko@gmail.com", "+38050-112-32-18", 2),
   ("Владіслав", "Харченко", "v.harchenko@gmail.com", "+38050-211-22-81", 1),
   ("Іван", "Воробйов", "i.vorobiyoff@gmail.com", "+38050-121-45-71", 1),
   ("Катерина", "Шамкало", "k.shamkalo@gmail.com", "+38066-331-67-99", 2),
   ("Віталій", "Козловський", "v.kozlovsky@gmail.com", "+38066-456-54-66", 1),
   ("Юлія", "Розгон", "j.rozgon@gmail.com", "+38066-555-66-12", 2),
   ("Тетяна", "Головач", "t.golovach@gmail.com", "+38050-551-16-21", 2),
   ("Артем", "Мірошниченко", "a.miroshnichenko@gmail.com", "+38066-888-56-87", 1),
   ("Євгенія", "Бондаренко", "e.bondarenko@gmail.com", "+38050-155-62-78", 2),
   ("Анастасія", "Тутук", "a.tutuk@gmail.com", "+38066-900-08-35", 2),
   ("Іван", "Челноков", "i.chelnokov@gmail.com", "+38068-454-77-34", 1),
   ("Маргарита", "Голубнича", "m.golubcha@gmail.com", "+38050-090-80-53", 2),
   ("Григорій", "Пивоваров", "g.pivovaroff@gmail.com", "+38066-441-67-54", 1),
   ("Андрій", "Носенко", "a.nosenko@gmail.com", "+38066-232-11-04", 1),
   ("Катерина", "Логвиненко", "k.logvinenko@gmail.com", "+38050-231-67-99", 2),
   ("Владислава", "Матьякубова", "v.matijakubova@gmail.com", "+38050-132-33-99", 2),
   ("Яна", "Євдокімова", "j.evdokimova@gmail.com", "+38067-144-33-99", 2),
   ("Максим", "Дудко", "m.dudko@gmail.com", "+38050-777-11-04", 1),
   ("Артур", "Гуденко", "a.gudenko@gmail.com", "+38067-666-22-04", 1),
   ("Владислав", "Колос", "v.kolos@gmail.com", "+38067-555-22-04", 1),
   ("Богдан", "Ващенко", "b.vaschenko@gmail.com", "+38068-444-22-04", 1),
   ("Руслан", "Вербицький", "r.verbitsky@gmail.com", "+38067-333-22-04", 1),
   ("Ілля", "Дейнека", "i.deyneka@gmail.com", "+38067-222-22-04", 1),
   ("Артем", "Юрченко", "a.yurchenko@gmail.com", "+38067-111-22-04", 1),
   ("Вікторія", "Сокура", "v.sokura@gmail.com", "+38055-114-33-99", 2),
   ("Владислав", "Трофименко", "v.trofimenko@gmail.com", "+38066-341-22-04", 1);
