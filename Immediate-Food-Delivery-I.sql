select round(100.0 * count(*) filter(where customer_pref_delivery_date = order_date) / count(*), 2) as immediate_percentage
from Delivery 