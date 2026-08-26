SELECT
    E.left_operand,
    E.operator,
    E.right_operand, 
    (CASE 
        WHEN E.operator = '>' THEN V1.value > V2.value
        WHEN E.operator = '<' THEN V1.value < V2.value
        ELSE V1.value = V2.value
    END) AS value
FROM expressions E
JOIN variables V1 ON E.left_operand = V1.name 
JOIN variables V2 ON E.right_operand = V2.name
