import pandas as pd
import numpy as np

def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
    w = orders['order_occurrences'].to_numpy()
    x = orders['item_count'].to_numpy()
    avg = round(float(np.average(x, weights=w)), 2) if w.sum() else None
    return pd.DataFrame({'average_items_per_order': [avg]})