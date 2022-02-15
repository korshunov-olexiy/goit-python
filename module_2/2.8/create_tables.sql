DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS genders;
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS teachers_subjects;
DROP TABLE IF EXISTS groups_subjects;


CREATE TABLE students (
	students_id INTEGER PRIMARY KEY,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	email VARCHAR(30) NOT NULL,
	phone VARCHAR(30) NOT NULL,
	genders_id INTEGER,
	grades_id INTEGER,
	subjects_id INTEGER,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT genders_FK FOREIGN KEY (genders_id) REFERENCES genders(genders_id) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT grades_FK FOREIGN KEY (grades_id) REFERENCES grades(grades_id) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT subjects_FK FOREIGN KEY (subjects_id) REFERENCES subjects(subjects_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE genders (
  genders_id INTEGER PRIMARY KEY,
  name VARCHAR(30),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE teachers (
  teachers_id INTEGER PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(40) NOT NULL UNIQUE,
  phone VARCHAR(30) NOT NULL UNIQUE,
  genders_id INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT genders_FK FOREIGN KEY (genders_id) REFERENCES genders(genders_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE subjects (
  subjects_id INTEGER PRIMARY KEY,
  name VARCHAR(80),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE teachers_subjects(
  id INTEGER PRIMARY KEY,
  teachers_id INTEGER,
  subjects_id INTEGER,
  CONSTRAINT teachers_FK FOREIGN KEY (teachers_id) REFERENCES teachers(teachers_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT subjects_FK FOREIGN KEY (subjects_id) REFERENCES subjects(subjects_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE groups (
  groups_id INTEGER PRIMARY KEY,
  name VARCHAR(80),
  students_id INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT students_FK FOREIGN KEY (students_id) REFERENCES students(students_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE groups_subjects (
  id INTEGER PRIMARY KEY,
  groups_id INTEGER,
  subjects_id INTEGER,
  CONSTRAINT groups_FK FOREIGN KEY (groups_id) REFERENCES groups(groups_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT subjects_FK FOREIGN KEY (subjects_id) REFERENCES subjects(subjects_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE grades (
  grades_id INTEGER PRIMARY KEY,
  value TINYINT UNSIGNED,
  maded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE lessons (
  lessons_id INTEGER PRIMARY KEY,
  students_id INTEGER,
  teachers_id INTEGER,
  groups_id INTEGER,
  started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT students_FK FOREIGN KEY (students_id) REFERENCES students(students_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT teachers_FK FOREIGN KEY (teachers_id) REFERENCES teachers(teachers_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT groups_FK FOREIGN KEY (groups_id) REFERENCES groups(groups_id) ON DELETE SET NULL ON UPDATE CASCADE
);

INSERT INTO genders (name) VALUES("male"), ("female");

INSERT INTO groups (name) VALUES("І-12"), ("ІМз-01с"), ("ІК.мз-11с");

INSERT INTO subjects (name) VALUES
   ("Технічна термодинаміка"),
   ("Основи охорони праці та БЖД"),
   ("Нормативно-правове забезпечення"),
   ("ДЗВ загальної підготовки"),
   ("Деталі машин");

INSERT INTO teachers (first_name, last_name, email, phone, genders_id) VALUES
  ("Андрій", "Євдокимов","a.yevdokymov@biem.sumdu.edu.ua","+38 (0542) 33-30-98", 1),
  ("Ольга","Лукаш","o.lukash@biem.sumdu.edu.ua","+38 (0542) 33-22-24", 2),
  ("Ірина","Дегтярьова","i.dehtyarova@biem.sumdu.edu.ua","+38 (0542) 33-22-23", 2);
