SELECT DISTINCT
    C.title
FROM content C
JOIN tv_program T ON C.content_id = T.content_id
WHERE 
    C.kids_content = 'Y' AND 
    C.content_type = 'Movies' AND
    T.program_date >= '2020-06-01' AND 
    T.program_date < '2020-07-01'