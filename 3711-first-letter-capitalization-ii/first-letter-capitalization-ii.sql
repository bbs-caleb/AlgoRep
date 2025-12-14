WITH RECURSIVE r AS (
  SELECT
    content_id,
    content_text,
    lower(content_text) AS s,
    97 AS code  -- 'a'
  FROM user_content

  UNION ALL

  SELECT
    content_id,
    content_text,
    regexp_replace(
      s,
      '(^|[ -])' || chr(code),
      E'\\1' || chr(code - 32),  
      'g'
    ) AS s,
    code + 1
  FROM r
  WHERE code <= 122 
)
SELECT
  content_id,
  content_text AS original_text,
  s AS converted_text
FROM r
WHERE code = 123    
ORDER BY content_id;
