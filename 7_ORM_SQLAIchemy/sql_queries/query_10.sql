-- 10. Список курсів, які певному студенту читає певний викладач.

SELECT Subjects.subject_name AS "предмет",
Students.student_name AS "Ім'я студента",
Teachers.teacher_name AS "викладач"
FROM Subjects
INNER JOIN Teachers ON Teachers.teacher_id = Subjects.teacher_id
INNER JOIN Grades ON Grades.subject_id = Subjects.subject_id
INNER JOIN Students ON Students.student_id = Grades.student_id
WHERE Students.student_id = 0 AND Subjects.teacher_id = 0
GROUP BY Subjects.subject_name