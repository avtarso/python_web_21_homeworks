-- 7. Знайти оцінки студентів у окремій групі з певного предмета.

SELECT Grades.grade AS "оцінка",
Students.student_name AS "Ім'я студента",
Groups.group_name AS "група",
Subjects.subject_name AS "предмет",
Grades.date AS "дата"
FROM Students
INNER JOIN Groups ON Groups.group_id = Students.group_id
INNER JOIN Grades ON Grades.student_id = Students.student_id
INNER JOIN Subjects ON Subjects.subject_id = Grades.subject_id
WHERE Groups.group_id = 0 AND Subjects.subject_id = 0
ORDER BY Students.student_name ASC