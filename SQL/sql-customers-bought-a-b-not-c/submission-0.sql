SELECT
    C.customer_id,
    C.customer_name
FROM customers C
WHERE 
    EXISTS (SELECT 1 FROM orders O WHERE O.customer_id = C.customer_id AND O.product_name = 'A') AND
    EXISTS (SELECT 1 FROM orders O WHERE O.customer_id = C.customer_id AND O.product_name = 'B') AND 
    NOT EXISTS (SELECT 1 FROM orders O WHERE O.customer_id = C.customer_id AND O.product_name = 'C')
ORDER BY C.customer_name ASC;