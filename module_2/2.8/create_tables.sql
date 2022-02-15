DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS genders;
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS classes;


CREATE TABLE students (
	students_id INTEGER PRIMARY KEY,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	email VARCHAR(30) NOT NULL,
	phone VARCHAR(30) NOT NULL,
	genders_id INTEGER,
	grades_id INTEGER,
	groups_id INTEGER,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT genders_FK FOREIGN KEY (genders_id) REFERENCES genders(genders_id) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT grades_FK FOREIGN KEY (grades_id) REFERENCES grades(grades_id) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT groups_FK FOREIGN KEY (groups_id) REFERENCES groups(groups_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE teachers (
  teachers_id INTEGER PRIMARY KEY,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  email VARCHAR(30) NOT NULL UNIQUE,
  phone VARCHAR(30) NOT NULL UNIQUE,
  genders_id INTEGER,
  subjects_id INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT genders_FK FOREIGN KEY (genders_id) REFERENCES genders(genders_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT subjects_FK FOREIGN KEY (subjects_id) REFERENCES subjects(subjects_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE genders (
  genders_id INTEGER PRIMARY KEY,
  name VARCHAR(30),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE grades (
  grades_id INTEGER PRIMARY KEY,
  value TINYINT UNSIGNED,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE groups (
  groups_id INTEGER PRIMARY KEY,
  name VARCHAR(80),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE subjects (
  subjects_id INTEGER PRIMARY KEY,
  name VARCHAR(80),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);