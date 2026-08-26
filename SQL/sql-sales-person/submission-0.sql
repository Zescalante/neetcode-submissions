SELECT
    P.name
FROM sales_person P 
WHERE NOT EXISTS (SELECT 1 FROM orders O JOIN company C ON O.com_id = C.com_id WHERE O.sales_id = P.sales_id AND C.name = 'CRIMSON')
-- JOIN orders O ON P.sales_id = O.sales_id 
-- JOIN company C ON C.com_id = O.com_id