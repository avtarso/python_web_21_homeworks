-- 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT AVG(Grades.grade) AS "середій бал",
Teachers.teacher_name AS "викладач",
Subjects.subject_name AS "предмет"
FROM Students
INNER JOIN Grades ON Grades.student_id = Students.student_id
INNER JOIN Subjects ON Subjects.subject_id = Grades.subject_id
INNER JOIN Teachers ON Teachers.teacher_id = Subjects.teacher_id
WHERE Teachers.teacher_id = 0
GROUP BY Subjects.subject_name