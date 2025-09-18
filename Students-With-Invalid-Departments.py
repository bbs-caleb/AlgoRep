import pandas as pd

def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
    invalid = (students
            .merge(departments, left_on='department_id', right_on='id', how='left', indicator=True)
            .query('_merge == "left_only"')[['id_x', 'name_x']]
            .rename(columns={'id_x': 'id', 'name_x': 'name'}))
    return invalid


    