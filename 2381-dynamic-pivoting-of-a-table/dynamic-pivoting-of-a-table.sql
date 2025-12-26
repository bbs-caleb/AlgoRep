CREATE PROCEDURE PivotProducts()
BEGIN
  SET SESSION group_concat_max_len = 1000000;

  SELECT
    GROUP_CONCAT(
      CONCAT(
        'MAX(CASE WHEN store = ''',
        REPLACE(store, '''', ''''''),
        ''' THEN price END) AS `',
        REPLACE(store, '`', '``'),
        '`'
      )
      ORDER BY store
      SEPARATOR ', '
    )
  INTO @cols
  FROM (SELECT DISTINCT store FROM Products) s;

  SET @sql = CONCAT(
    'SELECT product_id, ', @cols,
    ' FROM Products GROUP BY product_id'
  );

  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
END;
