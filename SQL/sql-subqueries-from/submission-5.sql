CREATE TABLE employees (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,
    salary INTEGER,
    department TEXT
);

INSERT INTO employees (name, salary, department) VALUES
  ('Alice', 50000, 'marketing'),
  ('Bob', 60000, 'marketing'),
  ('Charlie', 55000, 'marketing'),
  ('David', 65000, 'marketing'),
  ('Eve', 70000, 'finance'),
  ('Frank', 52000, 'finance'),
  ('Grace', 58000, 'finance'),
  ('Hank', 62000, 'finance');
-- Do not modify above this line. --


-- SELECT
--   E.name,
--   E.salary
-- FROM employees E
-- JOIN (
-- SELECT
--   AVG(salary) AS marketing_avg
-- FROM employees
-- WHERE department = 'marketing'
-- ) S ON E.salary < S.marketing_avg
-- WHERE department = 'marketing'
-- ORDER BY salary ASC;


SELECT
  name,
  salary
FROM (
SELECT
  name,
  salary,
  department,
  AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees
) AS S 
WHERE 
  department = 'marketing' AND 
  salary < dept_avg
ORDER BY salary ASC;