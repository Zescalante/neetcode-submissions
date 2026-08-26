SELECT 
    S.seller_name
FROM seller S 
WHERE NOT EXISTS (SELECT 1 FROM orders O WHERE sale_date BETWEEN '2020-01-01' AND '2020-12-31' AND O.seller_id = S.seller_id)
ORDER BY S.seller_name ASC