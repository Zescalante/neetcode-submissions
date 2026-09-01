WITH team_sizes AS (
SELECT  
    team_id,
    COUNT(*) AS team_size
FROM employee
GROUP BY team_id
)

SELECT
    E.employee_id,
    T.team_size
FROM employee E
JOIN team_sizes T ON E.team_id = T.team_id
