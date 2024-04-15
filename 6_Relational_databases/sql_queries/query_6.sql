-- 6. Знайти список студентів у певній групі.

SELECT Students.student_name AS "Ім'я студента",
Groups.group_name AS "група"
FROM Students
INNER JOIN Groups ON Groups.group_id = Students.group_id
WHERE Groups.group_id = 0
ORDER BY Students.student_name ASC