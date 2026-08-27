SELECT 
    user_id,
    time_stamp AS last_stamp
FROM (
SELECT 
    user_id,
    time_stamp,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY time_stamp DESC) AS rn
FROM logins
WHERE EXTRACT(YEAR FROM time_stamp::timestamp) = 2020
) AS S
WHERE rn = 1
