WITH stats AS (
SELECT
    student_id,
    exam_id,
    score,
    MAX(score) OVER (PARTITION BY exam_id) AS max_score,
    MIN(score) OVER (PARTITION BY exam_id) AS min_score
FROM exam 
),

non_extremes AS (
SELECT
    student_id,
    exam_id
FROM stats
-- GROUP BY student_id, exam_id
WHERE score <> max_score AND score <> min_score
)

SELECT
    N.student_id,
    S.student_name
FROM non_extremes N
JOIN student S ON S.student_id = N.student_id
GROUP BY 
    N.student_id,
    S.student_name
HAVING COUNT(N.exam_id) = (SELECT COUNT(*) FROM exam E WHERE E.student_id = N.student_id)
ORDER BY N.student_id ASC