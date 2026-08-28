SELECT
    customer_number
FROM (
SELECT
    customer_number,
    COUNT(*) AS order_cnt
FROM orders
GROUP BY customer_number
) AS S
ORDER BY order_cnt DESC
LIMIT 1