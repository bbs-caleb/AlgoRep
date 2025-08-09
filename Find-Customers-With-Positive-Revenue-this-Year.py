import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.loc[((customers['year'] == 2021) & (customers['revenue'] > 0)), ['customer_id']]