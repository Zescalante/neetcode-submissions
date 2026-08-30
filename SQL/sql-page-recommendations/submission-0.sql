WITH one_friends AS (
SELECT
    user1_id AS id
FROM friendship
WHERE user2_id = 1
UNION ALL
SELECT
    user2_id AS if
FROM friendship
WHERE user1_id = 1
)

SELECT DISTINCT
    L.page_id AS recommended_page
FROM one_friends F
JOIN likes L ON F.id = L.user_id
WHERE NOT EXISTS (SELECT 1 FROM likes L2 WHERE L2.user_id = 1 AND L.page_id = L2.page_id)