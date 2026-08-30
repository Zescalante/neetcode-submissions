WITH cte AS (
SELECT 
    seat_id,
    free,
    LAG(free) OVER (ORDER BY seat_id ASC) AS prev_free,
    LEAD(free) OVER (ORDER BY seat_id ASC) AS next_free
    -- seat_id - free AS increment
FROM cinema 
)
SELECT 
    seat_id
FROM cte
WHERE free = 1 AND (next_free = 1 OR prev_free = 1)
ORDER BY seat_id ASC