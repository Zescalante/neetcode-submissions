SELECT  
    department,
    employee,
    salary
FROM (
SELECT
    D.name AS department,
    E.name AS employee, 
    E.salary,
    DENSE_RANK() OVER (PARTITION BY D.id ORDER BY E.salary DESC) AS rnk
FROM department D
JOIN employee E ON D.id = E.department_id
) AS S
WHERE rnk = 1