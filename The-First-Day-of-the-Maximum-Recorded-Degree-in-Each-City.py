import pandas as pd

def find_the_first_day(weather: pd.DataFrame) -> pd.DataFrame:
    return (weather.sort_values(['city_id', 'degree', 'day'], ascending=[True, False, True])
                   .drop_duplicates(subset='city_id', keep='first')
                   .sort_values('city_id')[['city_id','day','degree']]
                   .reset_index(drop=True))