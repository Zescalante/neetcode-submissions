WITH prod_counts AS (
SELECT
    C.customer_id,
    O.product_id,
    COUNT(*) AS cnt
FROM customers C 
LEFT JOIN orders O ON C.customer_id = O.customer_id 
GROUP BY 
    C.customer_id,
    O.product_id
),

freqs AS (
SELECT
    customer_id,
    product_id,
    DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY cnt DESC) AS rnk
FROM prod_counts
)

SELECT
    F.customer_id,
    F.product_id,
    P.product_name
FROM freqs F
JOIN products P ON F.product_id = P.product_id
WHERE F.rnk = 1
