WITH gaps AS (
SELECT
    user_id,
    visit_date - LAG(visit_date) OVER (PARTITION BY user_id ORDER BY visit_date ASC) AS wind
    -- ('2021-01-01' - visit_date) AS today_diff
FROM user_visits
),

recent_gap AS (
SELECT
    user_id,
    ('2021-01-01' - MAX(visit_date)) AS today_diff
FROM user_visits
GROUP BY user_id 
)

SELECT
    G.user_id,
    GREATEST(MAX(G.wind), MAX(today_diff)) AS biggest_window
FROM gaps G
JOIN recent_gap R ON G.user_id = R.user_id 
GROUP BY G.user_id
ORDER BY G.user_id ASC


-- (SELECT
--     user_id,
--     GREATEST(MAX(biggest_window)) AS biggest_window
-- FROM gaps
-- GROUP BY user_id
-- HAVING COUNT(*) > 1)
-- UNION ALL
-- (SELECT
--     user_id,
--     MAX(today_diff) AS biggest_window
-- FROM gaps
-- GROUP BY user_id
-- HAVING COUNT(*) = 1)
-- ORDER BY user_id ASC