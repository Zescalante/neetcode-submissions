SELECT
    player_id,
    device_id
FROM
(SELECT
    player_id,
    device_id,
    ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS rn
FROM activity) AS S
WHERE rn = 1
