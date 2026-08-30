-- WITH all_stores AS (
-- SELECT 'store1' AS store
-- UNION 
-- SELECT 'store2' AS store
-- UNION
-- SELECT 'store3' AS store
-- )

-- SELECT  
--     product_id, 
--     store,
--     price
-- FROM (
-- SELECT
--     P.product_id,
--     S.store,
--     (CASE
--         WHEN S.store = 'store1' THEN P.store1
--         WHEN S.store = 'store2' THEN P.store2
--         WHEN S.store = 'store3' THEN P.store3
--     END) AS price
-- FROM products P
-- CROSS JOIN all_stores S
-- ) AS S
-- WHERE price IS NOT NULL
-- ORDER BY 
--     product_id ASC,
--     store ASC 


(SELECT  
    product_id, 
    'store1' AS store,
    store1 AS price
FROM products
WHERE store1 IS NOT NULL)
UNION 
(SELECT  
    product_id, 
    'store2' AS store,
    store2 AS price
FROM products
WHERE store2 IS NOT NULL) 
UNION 
(SELECT  
    product_id, 
    'store3' AS store,
    store3 AS price
FROM products
WHERE store3 IS NOT NULL) 