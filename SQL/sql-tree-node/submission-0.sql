SELECT
    id,
    (CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN NOT EXISTS (SELECT 1 FROM tree T2 WHERE T1.id = T2.p_id) THEN 'Leaf'
        ELSE 'Inner'
    END) AS type
FROM tree T1