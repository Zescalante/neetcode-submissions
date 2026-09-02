SELECT 
    project_id,
    employee_id
FROM 
(SELECT
    P.project_id,
    P.employee_id,
    DENSE_RANK() OVER (PARTITION BY P.project_id ORDER BY E.experience_years DESC) AS rnk
FROM project P 
JOIN employee E ON P.employee_id = E.employee_id) AS S
WHERE rnk = 1