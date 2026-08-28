SELECT
    U.name,
    SUM(amount) AS balance
FROM users U
JOIN transactions T ON U.account = T.account
GROUP BY U.name
HAVING SUM(amount) > 10000