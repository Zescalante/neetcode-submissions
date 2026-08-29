-- WITH june_orders AS (
-- SELECT
--     O.customer_id
-- FROM orders O
-- JOIN product P ON O.product_id = P.product_id
-- WHERE O.order_date >= '2020-06-01' AND O.order_date < '2020-07-01'
-- GROUP BY O.customer_id 
-- HAVING SUM(P.price*O.quantity) >= 100
-- ),
-- july_orders AS (
-- SELECT
--     O.customer_id
-- FROM orders O
-- JOIN product P ON O.product_id = P.product_id
-- WHERE O.order_date >= '2020-07-01' AND O.order_date < '2020-08-01'
-- GROUP BY O.customer_id 
-- HAVING SUM(P.price*O.quantity) >= 100
-- )

-- SELECT
--     J1.customer_id,
--     C.name
-- FROM june_orders J1 
-- JOIN july_orders J2 ON J1.customer_id = J2.customer_id
-- JOIN customers C ON J2.customer_id = C.customer_id


WITH cte AS (
SELECT
    O.customer_id,
    O.product_id,
    O.quantity,
    O.order_date,
    P.price
FROM orders O
JOIN product P ON O.product_id = P.product_id
WHERE O.order_date >= '2020-06-01' AND O.order_date < '2020-08-01'
)

SELECT
    C1.customer_id,
    C2.name
FROM cte C1 
JOIN customers C2 ON C1.customer_id = C2.customer_id
GROUP BY 
    C1.customer_id, 
    C2.name
HAVING 
    SUM(CASE WHEN C1.order_date >= '2020-06-01' AND C1.order_date < '2020-07-01' THEN C1.quantity*C1.price END) >= 100 AND 
    SUM(CASE WHEN C1.order_date >= '2020-07-01' AND C1.order_date < '2020-08-01' THEN C1.quantity*C1.price END) >= 100