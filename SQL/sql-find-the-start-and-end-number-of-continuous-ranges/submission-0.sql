WITH cte AS (
SELECT
    log_id, 
    ROW_NUMBER() OVER (ORDER BY log_id) AS counter,
    log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS diff
FROM logs
)

SELECT
    MIN(log_id) AS start_id,
    MAX(log_id) AS end_id
FROM cte
GROUP BY diff
ORDER BY start_id ASC