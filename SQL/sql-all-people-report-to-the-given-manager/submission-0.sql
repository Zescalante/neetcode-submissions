SELECT
    E1.employee_id
    -- E2.employee_id,
    -- E3.employee_id,
    -- E4.employee_id
FROM employees E1
LEFT JOIN employees E2 ON E1.manager_id = E2.employee_id
LEFT JOIN employees E3 ON E2.manager_id = E3.employee_id
LEFT JOIN employees E4 ON E3.manager_id = E4.employee_id
WHERE 
    E1.employee_id <> 1 AND 
    (E2.employee_id = 1 OR
    E3.employee_id = 1 OR
    E4.employee_id = 1)
