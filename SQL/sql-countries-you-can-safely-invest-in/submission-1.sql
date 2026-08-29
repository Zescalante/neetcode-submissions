WITH all_ids AS (
SELECT 
    caller_id AS id,
    duration
FROM calls 
UNION ALL
SELECT 
    callee_id AS id,
    duration
FROM calls 
),

country_calls AS (
SELECT
    C.name,
    A.duration,
    AVG(duration) OVER () AS global_avg
FROM all_ids A
JOIN person P ON A.id = P.id
JOIN country C ON LEFT(P.phone_number, 3) = C.country_code
)

SELECT
    name AS country
FROM country_calls
GROUP BY name
HAVING AVG(duration) > MAX(global_avg)