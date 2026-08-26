SELECT
    name
FROM customers C
WHERE NOT EXISTS (SELECT 1 FROM orders O WHERE C.id = O.customer_id)