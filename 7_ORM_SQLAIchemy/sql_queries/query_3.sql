-- 3. Знайти середній бал у групах з певного предмета.

SELECT AVG(Grades.grade) AS "середня oцінка",
Groups.group_name AS "група",
Subjects.subject_name AS "предмет"
FROM Grades
INNER JOIN Students ON Students.student_id = Grades.student_id
INNER JOIN Subjects ON Subjects.subject_id = Grades.subject_id
INNER JOIN Groups ON Groups.group_id = Students.group_id
WHERE Grades.subject_id = 1
GROUP by Students.group_id