-- SELECT 
--     user_id,
--     time_stamp AS last_stamp
-- FROM (
-- SELECT 
--     user_id,
--     time_stamp,
--     ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY time_stamp DESC) AS rn
-- FROM logins
-- WHERE EXTRACT(YEAR FROM time_stamp::timestamp) = 2020
-- ) AS S
-- WHERE rn = 1

SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM logins
WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
GROUP BY user_id
