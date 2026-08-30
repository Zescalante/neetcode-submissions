SELECT
    MIN(ABS(P1.x - P2.x)) AS shortest
FROM point P1
CROSS JOIN point P2
WHERE ABS(P1.x - P2.x) <> 0