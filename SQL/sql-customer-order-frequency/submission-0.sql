WITH june_orders AS (
SELECT
    O.customer_id
FROM orders O
JOIN product P ON O.product_id = P.product_id
WHERE O.order_date >= '2020-06-01' AND O.order_date < '2020-07-01'
GROUP BY O.customer_id 
HAVING SUM(P.price*O.quantity) >= 100
),
july_orders AS (
SELECT
    O.customer_id
FROM orders O
JOIN product P ON O.product_id = P.product_id
WHERE O.order_date >= '2020-07-01' AND O.order_date < '2020-08-01'
GROUP BY O.customer_id 
HAVING SUM(P.price*O.quantity) >= 100
)

SELECT
    J1.customer_id,
    C.name
FROM june_orders J1 
JOIN july_orders J2 ON J1.customer_id = J2.customer_id
JOIN customers C ON J2.customer_id = C.customer_id