from sqlalchemy import Date
from sqlalchemy import Integer, String, ForeignKey, create_engine, select, and_, or_, not_, desc, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column
from datetime import date

Base = declarative_base()

class Group(Base):
    __tablename__ = 'Groups'
    group_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    group_name: Mapped[str] = mapped_column(String(120))


class Student(Base):
    __tablename__ = 'Students'
    student_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_name: Mapped[str] = mapped_column(String(120))
    group_id: Mapped[int] = mapped_column(ForeignKey('Groups.group_id'))


class Teacher(Base):
    __tablename__ = 'Teachers'
    teacher_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    teacher_name: Mapped[str] = mapped_column(String(120))


class Subject(Base):
    __tablename__ = 'Subjects'
    subject_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject_name: Mapped[str] = mapped_column(String(120))
    teacher_id: Mapped[int] = mapped_column(ForeignKey('Teachers.teacher_id'))


class Grade(Base):
    __tablename__ = 'Grades'
    grade_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    grade_date: Mapped[date] = mapped_column(Date)
    grade: Mapped[int] = mapped_column(Integer)
    student_id: Mapped[int] = mapped_column(ForeignKey('Students.student_id'))
    subject_id: Mapped[int] = mapped_column(ForeignKey('Subjects.subject_id'))
    teacher_id: Mapped[int] = mapped_column(ForeignKey('Teachers.teacher_id'))
    
    