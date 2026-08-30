-- SELECT
--     E.employee_id
-- FROM employees E
-- WHERE 
--     E.name IS NULL OR
--     NOT EXISTS (SELECT 1 FROM salaries S WHERE S.employee_id = E.employee_id AND S.salary IS NOT NULL)
-- ORDER BY E.employee_id ASC
 
(SELECT
    E.employee_id
FROM employees E
WHERE NOT EXISTS (SELECT 1 FROM salaries S WHERE S.employee_id = E.employee_id))
UNION ALL
(SELECT
    S.employee_id
FROM salaries S
WHERE NOT EXISTS (SELECT 1 FROM employees E WHERE S.employee_id = E.employee_id))
ORDER BY employee_id ASC