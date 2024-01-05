-- Write your MySQL query statement below
SELECT st.student_id, st.student_name, su.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students st
CROSS JOIN Subjects su
LEFT JOIN Examinations e ON st.student_id = e.student_id AND su.subject_name = e.subject_name
GROUP BY st.student_id, st.student_name, su.subject_name
ORDER BY st.student_id, su.subject_name


-- Another solution found in the discussion section
SELECT st.student_id, st.student_name, su.subject_name, COALESCE(attended_exams, 0) AS attended_exams
FROM Students st
CROSS JOIN Subjects su
LEFT JOIN (SELECT student_id, subject_name, COUNT(*) AS attended_exams 
    FROM Examinations 
    GROUP BY student_id, subject_name) e USING (student_id, subject_name)
ORDER BY st.student_id, su.subject_name