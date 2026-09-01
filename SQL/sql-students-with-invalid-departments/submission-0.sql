SELECT
    id,
    name
FROM students S 
WHERE NOT EXISTS (SELECT 1 FROM departments D WHERE D.id = S.department_id)