import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    out = person.merge(address[['personId', 'city', 'state']],
            how = 'left', on = 'personId')
    return out[['firstName', 'lastName', 'city', 'state']]