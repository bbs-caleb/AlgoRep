import pandas as pd

def find_maximum_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['day_only'] = pd.to_datetime(transactions['day']).dt.date

    max_amount_per_day = transactions.groupby('day_only')['amount'].transform('max')

    result = transactions[transactions['amount'] == max_amount_per_day]

    result = result[['transaction_id']].sort_values('transaction_id').reset_index(drop=True)

    return result 