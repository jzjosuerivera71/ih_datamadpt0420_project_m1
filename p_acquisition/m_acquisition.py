import pandas as pd
from sqlalchemy import create_engine

# acquisition functions

#def acquire():
#    data = pd.read_csv('./data/raw/vehicles.csv')
#    return data

#Options: {'poll_info','country_info','personal_info','career_info'}
def acquire(string):
    engine = create_engine('sqlite:///C:\projects\\Data_tareas\\raw_data_project_m1.db')
    if string == 'poll_info':
        df_1 = pd.read_sql_query("SELECT * FROM poll_info", engine)
        return df_1 
    elif string == 'country_info':
        df_2 = pd.read_sql_query("SELECT * FROM country_info", engine)
        return df_2 
    elif string == 'personal_info':
        df_3 = pd.read_sql_query("SELECT * FROM personal_info", engine)
        return df_3
    elif string == 'career_info':
        df_4 = pd.read_sql_query("SELECT * FROM career_info", engine)
        return df_4
    
