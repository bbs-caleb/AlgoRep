import pandas as pd

def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    df = cities.sort_values(['state', 'city'])
    out = (df.groupby('state', as_index=False)['city']
             .agg(lambda s: ', '.join(s)))
    return out.rename(columns={'city': 'cities'})
