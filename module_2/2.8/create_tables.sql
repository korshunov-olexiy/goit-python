DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS genders;
DROP TABLE IF EXISTS groups_students;


CREATE TABLE departments (
	department_id INTEGER PRIMARY KEY,
	name VARCHAR(80)
);

CREATE TABLE groups (
  group_id INTEGER PRIMARY KEY,
  name VARCHAR(80),
  department_id INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT departments_FK FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE lessons (
  lesson_id INTEGER PRIMARY KEY,
  subject_id INTEGER,
  student_id INTEGER,
  teacher_id INTEGER,
  grade INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT students_FK FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT teachers_FK FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT subjects_FK FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE subjects (
  subject_id INTEGER PRIMARY KEY,
  name VARCHAR(80)
);

CREATE TABLE teachers (
  teacher_id INTEGER PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(40) NOT NULL UNIQUE,
  phone VARCHAR(20) NOT NULL UNIQUE,
  gender_id INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT genders_FK FOREIGN KEY (gender_id) REFERENCES genders(gender_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE students (
	student_id INTEGER PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(40) NOT NULL,
	phone VARCHAR(20) NOT NULL,
	gender_id INTEGER,
	group_id INTEGER,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT genders_FK FOREIGN KEY (gender_id) REFERENCES genders(gender_id) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT groups_FK FOREIGN KEY (group_id) REFERENCES groups(group_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE genders (
  gender_id INTEGER PRIMARY KEY,
  name VARCHAR(30)
);
