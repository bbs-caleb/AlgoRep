1import pandas as pd
2
3def team_size(employee: pd.DataFrame) -> pd.DataFrame:
4    employee['team_size'] = employee.groupby('team_id')['employee_id'].transform('size')
5    return employee[['employee_id', 'team_size']]