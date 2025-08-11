import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    out = (activity.sort_values(['player_id', 'event_date'])
             .drop_duplicates(subset='player_id', keep='first')
             [['player_id', 'event_date']]
             .rename(columns={'event_date': 'first_login'}))
    return out