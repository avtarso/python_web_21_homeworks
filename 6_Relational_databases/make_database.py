import sqlite3
from faker import Faker
import random
from datetime import date, timedelta
from pathlib import Path
import os


DATABASE = "grades_database.db"
STUDENTS_QUANTITY = 50

TEACHERS_QUANTITY = 4
SUBJECTS_QUANTITY = 5
LESSONS_QUANTITY = 20


def create_database(database):

    if  not os.path.isfile(DATABASE):
        Path(DATABASE).touch()
    
    with sqlite3.connect(database) as db:
        c = db.cursor()

        c.execute('''
                        CREATE TABLE "Groups" (
                            "group_id"	INTEGER,
                            "group_name"	TEXT,
                            PRIMARY KEY("group_id" AUTOINCREMENT)
                        );''')        

        c.execute('''
                        CREATE TABLE "Students" (
                            "student_id"	INTEGER,
                            "student_name"	TEXT,
                            "group_id"	INTEGER,
                            FOREIGN KEY("group_id") REFERENCES "Groups"("group_id"),
                            PRIMARY KEY("student_id" AUTOINCREMENT)
                        );''')
        c.execute('''
                        CREATE TABLE "Teachers" (
                            "teacher_id"	INTEGER,
                            "teacher_name"	TEXT,
                            PRIMARY KEY("teacher_id" AUTOINCREMENT)
                        );''')                
        
        c.execute('''
                        CREATE TABLE "Subjects" (
                            "subject_id"	INTEGER,
                            "subject_name"	TEXT,
                            "teacher_id"	INTEGER,
                            PRIMARY KEY("subject_id" AUTOINCREMENT),
                            FOREIGN KEY("teacher_id") REFERENCES "Teachers"("teacher_id")
                        );''')        

        c.execute('''
                        CREATE TABLE "Grades" (
                            "grade_id"	INTEGER,
                            "student_id"	INTEGER,
                            "subject_id"	INTEGER,
                            "teacher_id"	INTEGER,
                            "date"	TEXT,
                            "grade"	INTEGER,
                            FOREIGN KEY("teacher_id") REFERENCES "Teachers"("teacher_id"),
                            PRIMARY KEY("grade_id" AUTOINCREMENT),
                            FOREIGN KEY("subject_id") REFERENCES "Subjects"("subject_id"),
                            FOREIGN KEY("student_id") REFERENCES "Students"("student_id")
                        );''')
        db.commit()


def pill_database(database):

    fake = Faker(['uk_UA'])

    groups = ["MT-2024", "EN-2024", "ТК-2024"]
    groups_quantity = len(groups)

    with sqlite3.connect(database) as db:
        c = db.cursor()
        for i in range(len(groups)):
            c.execute('''INSERT INTO Groups (group_id, group_name) 
                    VALUES (?, ?)''',
                    (i, groups[i])
                )
        db.commit()


    with sqlite3.connect(database) as db:
        c = db.cursor()
        for i in range(STUDENTS_QUANTITY):
            c.execute('''INSERT INTO Students (student_id, student_name, group_id) 
                    VALUES (?, ?, ?)''',
                    (i, fake.name(), random.randint(0, groups_quantity - 1))
                )
        db.commit()


    with sqlite3.connect(database) as db:
        c = db.cursor()
        for i in range(TEACHERS_QUANTITY):
            c.execute('''INSERT INTO Teachers (teacher_id, teacher_name) 
                    VALUES (?, ?)''',
                    (i, fake.name())
                )
        db.commit()


    subjects = ["Дизайн та поведінка", "Теорія ігор", "Безпека мереж", "Машинне навчання", "Основи штучного інтелекту"]
    subjects_quantity = len(subjects)

    with sqlite3.connect(database) as db:
        c = db.cursor()
        for i in range(subjects_quantity):
            c.execute('''INSERT INTO Subjects (subject_id, subject_name, teacher_id) 
                    VALUES (?, ?, ?)''',
                    (i, subjects[i], i%TEACHERS_QUANTITY)
                )
        db.commit()


    with sqlite3.connect(database) as db:
        
        c = db.cursor()
        c.execute('''SELECT * FROM Subjects''')
        subject_list = c.fetchall()

        grade_i = 0
        deltatime = timedelta(days=7)
        exam_date = date.today() - LESSONS_QUANTITY * deltatime
        
        for k_time in range(LESSONS_QUANTITY):

            date_to_table = exam_date + k_time * deltatime

            for subject in range(len(subject_list)):

                c.execute('''SELECT student_id FROM Students''')
                student_list = c.fetchall()

                for student in range(len(student_list)):

                    c.execute('''INSERT INTO Grades (grade_id, student_id, subject_id, teacher_id, date, grade) 
                        VALUES (?, ?, ?, ?, ?, ?)''',
                        (grade_i, student_list[student][0], subject_list[subject][0], subject_list[subject][1], date_to_table, random.randint(3, 5))
                    )
                    grade_i += 1
        db.commit()

def make_ready_database(database):

    create_database(database)
    pill_database(database)

make_ready_database(DATABASE)   