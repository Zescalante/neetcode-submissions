WITH recent_orders AS (
SELECT
    order_date,
    customer_id,
    order_id,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
FROM orders
)

SELECT
    C.name AS customer_name,
    C.customer_id,
    R.order_id,
    R.order_date
FROM recent_orders R
JOIN customers C ON R.customer_id = C.customer_id
WHERE R.rn <= 3
ORDER BY 
    customer_name ASC,
    C.customer_id ASC,
    R.order_date DESC