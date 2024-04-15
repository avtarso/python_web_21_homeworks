-- 5. Знайти які курси читає певний викладач.

SELECT subject_name AS "предмет",
Teachers.teacher_name AS "викладач"
FROM Subjects
INNER JOIN Teachers ON Teachers.teacher_id = Subjects.teacher_id
WHERE Teachers.teacher_id = 0