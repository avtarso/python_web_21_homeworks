"""
a set of different database queries
"""

from sqlalchemy.orm import aliased
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, func

from classes import Base, Group, Student, Teacher, Subject, Grade
from functions import get_session, get_id_item
from settings import DATABASE

def select_1(session):
    
    name_select = '''1. Find the 5 students with the highest average score in all subjects'''

    avg_grade = func.avg(Grade.grade).label('average_grade')
    
    query = (
        session.query(
            Student.student_name,
            Group.group_name,
            avg_grade
        )
        .join(Grade, Grade.student_id == Student.student_id)
        .join(Group, Group.group_id == Student.group_id)
        .group_by(
            Student.student_name, 
            Group.group_name
        )
        .order_by(avg_grade.desc())
        .limit(5)
    )
    return query.all(), name_select


def select_2(session):

    name_select = '''2. Find the student with the highest average score in a certain subject'''

    target_subject_id = get_id_item(session, Subject.subject_id, Subject.subject_name, Subject)

    avg_grade = func.avg(Grade.grade)

    query = (
        session.query(
            Student.student_name,
            Group.group_name,
            Subject.subject_name,
            avg_grade
        )
        .join(Student, Student.student_id == Grade.student_id)
        .join(Subject, Subject.subject_id == Grade.subject_id)
        .join(Group, Group.group_id == Student.group_id)
        .filter(Grade.subject_id == target_subject_id) 
        .group_by(
            Student.student_name,
            Group.group_name,
            Subject.subject_name            
        )
        .order_by(avg_grade.desc())
        .limit(1)
    )
    return query.all(), name_select


def select_3(session):

    name_select = '''. Find the average score in groups for a certain subject'''

    target_subject_id = get_id_item(session, Subject.subject_id, Subject.subject_name, Subject)

    query = (
        session.query(
            func.avg(Grade.grade),
            Group.group_name,
            Subject.subject_name
        )
        .join(Student, Student.student_id == Grade.student_id)
        .join(Subject, Subject.subject_id == Grade.subject_id)
        .join(Group, Group.group_id == Student.group_id)
        .filter(Grade.subject_id == target_subject_id) 
        .group_by(
            Group.group_name,
            Subject.subject_name
            )
    )
    return query.all(), name_select


def select_4(session):

    name_select = '''4. Find the average score on the stream (over the entire score table)'''

    query = (
        session.query(func.avg(Grade.grade)
        )
    )
    return query.all(), name_select


def select_5(session):

    name_select = '''5. Find which courses a certain teacher teaches'''

    target_teacher_id = get_id_item(session, Teacher.teacher_id, Teacher.teacher_name, Teacher)

    query = (
        session.query(
            Subject.subject_name,
            Teacher.teacher_name
        )
        .join(Teacher, Teacher.teacher_id == Subject.teacher_id)
        .filter(Teacher.teacher_id == target_teacher_id) 
    )
    return query.all(), name_select


def select_6(session):

    name_select = '''6. Find a list of students in a certain group'''

    target_group_id = get_id_item(session, Group.group_id, Group.group_name, Group)

    query = (
        session.query(
            Student.student_name,
            Group.group_name
        )
        .join(Group, Group.group_id == Student.group_id)
        .filter(Group.group_id == target_group_id)
        .order_by(Student.student_name.asc())
    )
    return query.all(), name_select


def select_7(session):

    name_select = '''7. Find the grades of students in a separate group on a certain subject'''

    target_subject_id = get_id_item(session, Subject.subject_id, Subject.subject_name, Subject)
    target_group_id = get_id_item(session, Group.group_id, Group.group_name, Group)

    query = (
        session.query(
            Grade.grade,
            Grade.grade_date,
            Student.student_name,
            Group.group_name,
            Subject.subject_name,
        )
        .join(Grade, Grade.student_id == Student.student_id)
        .join(Group, Group.group_id == Student.group_id)
        .join(Subject, Subject.subject_id == Grade.subject_id)
        .filter(
            Group.group_id == target_group_id,
            Subject.subject_id == target_subject_id
        )
        .order_by(Student.student_name.asc())
    )
    return query.all(), name_select 


def select_8(session):

    name_select = '''8. Find the average score given by a certain teacher in his subjects'''

    target_teacher_id = get_id_item(session, Teacher.teacher_id, Teacher.teacher_name, Teacher)

    query = (
        session.query(
            func.avg(Grade.grade),
            Teacher.teacher_name,
            Subject.subject_name
        )
        .join(Subject, Subject.subject_id == Grade.subject_id)
        .join(Teacher, Teacher.teacher_id == Grade.teacher_id)
        .filter(Teacher.teacher_id == target_teacher_id)
        .group_by(
            Teacher.teacher_name,
            Subject.subject_name
        )
    )
    return query.all(), name_select


def select_9(session):

    name_select = '''9. Find the list of courses attended by the student'''

    target_student_id = get_id_item(session, Student.student_id, Student.student_name, Student)

    query = (
        session.query(
            Subject.subject_name,
            Student.student_name
        )
        .join(Grade, Grade.subject_id == Subject.subject_id)
        .join(Student, Student.student_id == Grade.student_id)
        .filter(Grade.student_id == target_student_id)
        .group_by(
            Subject.subject_name,
            Student.student_name
        )
    )
    return query.all(), name_select


def select_10(session):

    name_select = '''10. A list of courses taught to a particular student by a particular teacher'''

    target_teacher_id = get_id_item(session, Teacher.teacher_id, Teacher.teacher_name, Teacher)
    target_student_id = get_id_item(session, Student.student_id, Student.student_name, Student)

    query = (
        session.query(
            Subject.subject_name,
            Student.student_name,
            Teacher.teacher_name
        )
        .join(Teacher, Teacher.teacher_id == Subject.teacher_id)
        .join(Grade, Grade.subject_id == Subject.subject_id)
        .join(Student, Student.student_id == Grade.student_id)
        .filter(
            Student.student_id == target_student_id,
            Grade.teacher_id == target_teacher_id)
        .group_by(
            Subject.subject_name, 
            Student.student_name, 
            Teacher.teacher_name
        )
    )
    return query.all(), name_select


def select_11(session):

    name_select = '''11. The average score given by a certain teacher to a certain student'''

    target_teacher_id = get_id_item(session, Teacher.teacher_id, Teacher.teacher_name, Teacher)
    target_student_id = get_id_item(session, Student.student_id, Student.student_name, Student)

    query = (
        session.query(
            func.avg(Grade.grade),
            Student.student_name,
            Teacher.teacher_name
        )
        .join(Student, Student.student_id == Grade.student_id)
        .join(Teacher, Teacher.teacher_id == Grade.teacher_id)
        .filter(
            Grade.student_id == target_student_id,
            Grade.teacher_id == target_teacher_id)
    )
    return query.all(), name_select


def select_12(session):

    name_select = '''12. Grades of students in a certain group on a certain subject in the last lesson'''

    target_subject_id = get_id_item(session, Subject.subject_id, Subject.subject_name, Subject)
    target_group_id = get_id_item(session, Group.group_id, Group.group_name, Group)

    subquery = (
        session.query(
            func.count(Student.student_id)
        )
        .filter(Student.group_id == target_group_id)
        .scalar_subquery()
    )
    query = (
        session.query(
            Grade.grade,
            Student.student_name,
            Group.group_name,
            Subject.subject_name,
            Grade.grade_date
        )
        .join(Student, Student.student_id == Grade.student_id)
        .join(Group, Group.group_id == Student.group_id)
        .join(Subject, Subject.subject_id == Grade.subject_id)
        .filter(
            Group.group_id == target_group_id, 
            Subject.subject_id == target_subject_id
        )
        .order_by(
            Grade.grade_date.desc(), 
            Student.student_name.asc()
        )
        .limit(subquery)
    )
    return query.all(), name_select