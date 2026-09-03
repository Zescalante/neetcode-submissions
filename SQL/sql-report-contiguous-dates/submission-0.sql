WITH filtered_dates AS (
SELECT
    fail_date AS "date",
    0 AS success
FROM failed
WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
UNION ALL 
SELECT
    success_date AS "date",
    1 AS success
FROM succeeded
WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
),

lagged_dates AS (
SELECT 
    date,
    success, 
    LAG(success) OVER (ORDER BY date ASC) AS prev_success
FROM filtered_dates
),

periods AS (
SELECT
    date, 
    (CASE WHEN (success <> prev_success OR prev_success IS NULL) THEN 1 ELSE 0 END) AS new_period,
    success
FROM lagged_dates
)

SELECT
    (CASE WHEN MAX(success) = 1 THEN 'succeeded' ELSE 'failed' END) AS period_state,
    MIN(date) AS start_date,
    MAX(date) AS end_date
FROM  (
SELECT
    date, 
    SUM(new_period) OVER (ORDER BY date ASC) AS period_id,
    success
FROM periods
) AS S
GROUP BY period_id 
ORDER BY start_date ASC