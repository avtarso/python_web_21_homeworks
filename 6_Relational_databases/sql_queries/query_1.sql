-- 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT Students.student_name AS "Ім'я студента",
Groups.group_name AS "група",
AVG(Grades.grade) AS "середня oцінка"
FROM Grades
INNER JOIN Students ON Students.student_id = Grades.student_id
INNER JOIN Groups ON Groups.group_id = Students.group_id
GROUP by Students.student_id
ORDER BY AVG(Grades.grade) DESC
LIMIT 5