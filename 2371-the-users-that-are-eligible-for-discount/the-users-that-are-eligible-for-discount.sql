CREATE OR REPLACE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT)
RETURNS TABLE (user_id INT) AS $$
BEGIN
  RETURN QUERY (
      with cte as (
    select p.user_id, p.time_stamp::date, sum(case when amount >= minAmount then 1 else 0 end) as total 
    from Purchases p
    where time_stamp between startDate and endDate 
    group by 1, 2
    )
    select distinct p.user_id
    from cte p 
    where total > 0

  );
END;
$$ LANGUAGE plpgsql;