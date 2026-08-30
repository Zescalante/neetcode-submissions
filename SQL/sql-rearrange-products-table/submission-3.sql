WITH all_stores AS (
SELECT 'store1' AS store
UNION 
SELECT 'store2' AS store
UNION
SELECT 'store3' AS store
)

SELECT  
    product_id, 
    store,
    price
FROM (
SELECT
    P.product_id,
    S.store,
    (CASE
        WHEN S.store = 'store1' THEN P.store1
        WHEN S.store = 'store2' THEN P.store2
        WHEN S.store = 'store3' THEN P.store3
    END) AS price
FROM products P
CROSS JOIN all_stores S
) AS S
WHERE price IS NOT NULL
ORDER BY 
    product_id ASC,
    store ASC 
