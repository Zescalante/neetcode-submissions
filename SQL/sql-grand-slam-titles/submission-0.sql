WITH all_wins AS (
SELECT wimbledon AS winner
FROM championships
UNION ALL
SELECT fr_open AS winner
FROM championships
UNION ALL
SELECT us_open AS winner
FROM championships
UNION ALL
SELECT au_open AS winner
FROM championships
)

SELECT
    P.player_id,
    P.player_name,
    COUNT(*) AS grand_slams_count
FROM all_wins A
JOIN players P ON A.winner = P.player_id
GROUP BY 
    P.player_id,
    P.player_name