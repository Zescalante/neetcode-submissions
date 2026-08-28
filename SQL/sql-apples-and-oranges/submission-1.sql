SELECT
    sale_date,
    MAX(CASE WHEN fruit = 'apples' THEN sold_num END) -
    MAX(CASE WHEN fruit = 'oranges' THEN sold_num END) AS diff
FROM sales
GROUP BY sale_date
ORDER BY sale_date ASC