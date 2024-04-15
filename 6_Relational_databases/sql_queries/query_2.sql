-- 2. Знайти студента із найвищим середнім балом з певного предмета.

SELECT Students.student_name AS "Ім'я студента",
Groups.group_name AS "група",
Subjects.subject_name AS "предмет",
AVG(Grades.grade) AS "найвища середня oцінка"
FROM Grades
INNER JOIN Students ON Students.student_id = Grades.student_id
INNER JOIN Subjects ON Subjects.subject_id = Grades.subject_id
INNER JOIN Groups ON Groups.group_id = Students.group_id
WHERE Grades.subject_id = 1
GROUP by Students.student_id
ORDER BY AVG(Grades.grade) DESC
LIMIT 1