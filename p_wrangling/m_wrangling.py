import pandas as pd

# wrangling functions

def Cleaning_Dataframe_1(df_4):
    
    Serie_uuid = df_4['uuid']
    Serie_dem_education_level = df_4['dem_education_level']
    Serie_dem_full_time_job = df_4['dem_full_time_job']
    Serie_normalized_job_code = df_4['normalized_job_code']
    #
    lst_uuid = list(Serie_uuid)
    lst_dem_education_level = list(Serie_dem_education_level)
    lst_dem_full_time_job = list(Serie_dem_full_time_job)
    lst_normalized_job_code = list(Serie_normalized_job_code)
    #
    size_normalized_job_code = len(lst_normalized_job_code)
    clean_normalized_job_code = [[i,lst_uuid[i],lst_dem_education_level[i],lst_dem_full_time_job[i],lst_normalized_job_code[i]] for i in range(size_normalized_job_code) if lst_normalized_job_code[i] != None]
    
    colnames = ['previous_index','uuid','dem_education_level','dem_full_time_job','normalized_job_code']

    new_df = pd.DataFrame(clean_normalized_job_code, columns=colnames)
    
    return new_df
    
    
def Merge(df_2,df_3,df_4,Cl_df_4):
    #
    # listing table country_info
    lst_country = list(df_2['country_code'])
    #
    #listing table personal_info
    lst_gender = list(df_3['gender'])
    #
    #listing table career_info
    lst_previous_index = list(Cl_df_4['previous_index'])
    lst_uuid=list(df_4['uuid'])
    lst_normalized_job_code= list(df_4['normalized_job_code'])
    #
    #listing table clean_career_info
    lst_previous_index = list(Cl_df_4['previous_index'])
    # New Dataframe
    lst_lst = [[lst_uuid[i], lst_gender[i] ,lst_country[i], lst_normalized_job_code[i]] for i in lst_previous_index]
    colnames = ['uuid','gender','country_code','normalized_job_code']
    new_df = pd.DataFrame(lst_lst, columns=colnames)
    return new_df
