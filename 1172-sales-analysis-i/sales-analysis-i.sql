SELECT seller_id
FROM (
    SELECT seller_id,
           SUM(quantity * price) AS total_sales,
           rank() OVER (ORDER BY SUM(price) desc) AS rnk
    FROM Sales
    GROUP BY seller_id
) t
WHERE rnk = 1;
