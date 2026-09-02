-- SELECT
--     transaction_id
-- FROM 
-- (SELECT
--     transaction_id,
--     DENSE_RANK() OVER (PARTITION BY DATE(day) ORDER BY amount DESC) AS rnk 
-- FROM transactions) AS S
-- WHERE rnk = 1
-- ORDER BY transaction_id ASC

SELECT  
    transaction_id
FROM transactions
WHERE (DATE(day), amount) IN 
    (SELECT DATE(day), MAX(amount) FROM transactions GROUP BY DATE(day))
ORDER BY transaction_id ASC