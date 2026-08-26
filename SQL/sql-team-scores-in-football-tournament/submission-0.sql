WITH splits AS (
SELECT
    host_team as team_id,
    (CASE 
        WHEN host_goals > guest_goals THEN 3
        WHEN host_goals = guest_goals THEN 1
        ELSE 0
    END) AS num_points
FROM matches
UNION ALL
SELECT
    guest_team as team_id,
    (CASE 
        WHEN host_goals < guest_goals THEN 3
        WHEN host_goals = guest_goals THEN 1
        ELSE 0
    END) AS num_points
FROM matches
)

SELECT
    T.team_id,
    T.team_name,
    COALESCE(SUM(S.num_points), 0) AS num_points
FROM teams T
LEFT JOIN splits S ON T.team_id = S.team_id
GROUP BY 
    T.team_id,
    T.team_name
ORDER BY 
    num_points DESC,
    T.team_id ASC