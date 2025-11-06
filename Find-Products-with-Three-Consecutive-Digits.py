import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask = products['name'].str.contains(r'(?<!\d)\d{3}(?!\d)', regex=True, na=False)
    out = products.loc[mask, ['product_id', 'name']].sort_values('product_id').reset_index(drop=True)
    return out
