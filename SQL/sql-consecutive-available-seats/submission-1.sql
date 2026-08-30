-- WITH cte AS (
-- SELECT 
--     seat_id,
--     free,
--     LAG(free) OVER (ORDER BY seat_id ASC) AS prev_free,
--     LEAD(free) OVER (ORDER BY seat_id ASC) AS next_free
-- FROM cinema 
-- )
-- SELECT 
--     seat_id
-- FROM cte
-- WHERE free = 1 AND (next_free = 1 OR prev_free = 1)
-- ORDER BY seat_id ASC

SELECT DISTINCT
    C1.seat_id 
FROM cinema C1
JOIN cinema C2 ON ABS(C1.seat_id - C2.seat_id) = 1
WHERE 
    C1.free = 1 AND 
    C2.free = 1
ORDER BY C1.seat_id ASC