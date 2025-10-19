SELECT buyer_id
FROM Sales s
JOIN Product p ON s.product_id = p.product_id
WHERE p.product_name IN ('S8', 'iPhone')
GROUP BY buyer_id
HAVING 
  COUNT(*) FILTER (WHERE p.product_name = 'S8') > 0
  AND COUNT(*) FILTER (WHERE p.product_name = 'iPhone') = 0;



