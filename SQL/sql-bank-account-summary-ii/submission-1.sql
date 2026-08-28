SELECT
    U.name,
    SUM(T.amount) AS balance
FROM users U
JOIN transactions T ON U.account = T.account
GROUP BY U.name
HAVING SUM(T.amount) > 10000