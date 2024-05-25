"""
This module is used to fill a database with fictitious values for testing 
and learning.

It creates tables for groups, students, teachers, subjects and grades, 
and then writes random data to them.
"""

from datetime import date, timedelta
from faker import Faker
import logging
import random

from classes import Base, Group, Student, Teacher, Subject, Grade
from functions import get_session
from settings import DATABASE


# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

STUDENTS_QUANTITY = 50
TEACHERS_QUANTITY = 4
LESSONS_QUANTITY = 20

groups = ["MT-2024", 
          "EN-2024", 
          "ТК-2024"]
subjects = ["Дизайн та поведінка",
            "Теорія ігор", 
            "Безпека мереж", 
            "Машинне навчання", 
            "Основи штучного інтелекту"]

fake = Faker(['uk_UA'])

def fill_groups(session):
    """Fills the groups table in the database.

     Args:
         session (Session): SQLAlchemy session.
     """
    logger.info("Filling groups")
    for group_name in groups:
        group = Group(group_name=group_name)
        session.add(group)

def fill_students(session):
    """Fills the student table in the database.

     Args:
         session (Session): SQLAlchemy session.
     """
    logger.info("Filling Student")
    group_ids = session.query(Group.group_id).all()
    for _ in range(STUDENTS_QUANTITY):
        student = Student(student_name=fake.name(), group_id=random.choice(group_ids)[0])
        session.add(student)

def fill_teachers(session):
    """Fills the teachers table in the database.

     Args:
         session (Session): SQLAlchemy session.
     """
    logger.info("Filling Teachers")
    for _ in range(TEACHERS_QUANTITY):
        teacher = Teacher(teacher_name=fake.name())
        session.add(teacher)

def fill_subjects(session):
    """Fills a table of items in the database.

     Args:
         session (Session): SQLAlchemy session.
     """
    logger.info("Filling Subjects")
    teacher_ids = session.query(Teacher.teacher_id).all()
    for i, subject_name in enumerate(subjects):
        subject = Subject(subject_name=subject_name, teacher_id=random.choice(teacher_ids)[0])
        session.add(subject)

def fill_grades(session):
    """Fills out the ratings table in the database.

     Args:
         session (Session): SQLAlchemy session.
     """
    logger.info("Filling Grades")
    student_ids = session.query(Student.student_id).all()
    subject_ids = session.query(Subject.subject_id, Subject.teacher_id).all()
    deltatime = timedelta(days=7)       # 1 lesson per 7 days
    date_lessons_start = date.today() - LESSONS_QUANTITY * deltatime

    for k_time in range(LESSONS_QUANTITY):
        date_to_table = date_lessons_start + k_time * deltatime
        for subject_id in subject_ids:
            for student_id in student_ids:
                grade = Grade(
                    student_id=student_id[0], 
                    subject_id=subject_id[0], 
                    teacher_id=subject_id[1], 
                    grade_date=date_to_table, 
                    grade=random.randint(3, 5)
                )
                session.add(grade)

def main():
    """The main function of fake filling the database."""
    with get_session(DATABASE) as session:
        fill_groups(session)
        fill_students(session)
        fill_teachers(session)
        fill_subjects(session)
        fill_grades(session)
        session.commit()
        logger.info("Database filled successfully")

if __name__ == '__main__':
    main()
