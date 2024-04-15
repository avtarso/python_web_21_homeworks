-- 9. Знайти список курсів, які відвідує студент.

SELECT Subjects.subject_name AS "предмет",
Students.student_name AS "Ім'я студента"
FROM Subjects
INNER JOIN Grades ON Grades.subject_id = Subjects.subject_id
INNER JOIN Students ON Students.student_id = Grades.student_id
WHERE Grades.student_id = 0
GROUP BY Subjects.subject_name