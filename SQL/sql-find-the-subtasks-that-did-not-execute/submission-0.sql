WITH RECURSIVE series AS (
SELECT 1 AS val
UNION ALL
SELECT val + 1
FROM series
WHERE val < 20
)

SELECT
    T.task_id,
    -- T.subtasks_count,
    S.val AS subtask_id
    -- E.subtask_id
FROM tasks T
JOIN series S ON S.val <= T.subtasks_count
LEFT JOIN executed E ON E.task_id = T.task_id AND E.subtask_id = S.val
WHERE E.subtask_id IS NULL
-- E.subtask_id <> S.val