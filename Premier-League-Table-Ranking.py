import pandas as pd

def calculate_team_standings(team_stats: pd.DataFrame) -> pd.DataFrame:
    df = team_stats.copy()
    df['points'] = df['wins'] * 3 + df['draws']
    df['position'] = df['points'].rank(method='min', ascending=False).astype(int)
    out = df.sort_values(['points', 'team_name'], ascending=[False, True])
    return out[['team_id', 'team_name', 'points', 'position']]
