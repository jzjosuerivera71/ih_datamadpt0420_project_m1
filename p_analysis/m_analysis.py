import pandas as pd

# analysis functions

def Analisis_1(merge_df):
    #listing
    lst_gender = list(merge_df['gender'])
    lst_country_code = list(merge_df['country_code'])
    #Set
    set_country_code = set(lst_country_code)
    #
    # Listing Set
    lst_set_country_code = list(set_country_code)
    #Size
    size_lst_gender = len(lst_gender)
    size_lst_set_country_code = len(lst_set_country_code)
    #
    #Listing genders
    female_lst = [[i,lst_gender[i],lst_country_code[i]] for i in range(size_lst_gender) if lst_gender[i][0]== 'f' or lst_gender[i][0]== 'F']
    male_lst = [[i,lst_gender[i],lst_country_code[i]] for i in range(size_lst_gender) if lst_gender[i][0] == 'm' or lst_gender[i][0] == 'M']
    #
    #initialization
    lst_M = [ [] for i in range(size_lst_set_country_code)] 
    lst_F = [ [] for i in range(size_lst_set_country_code)] 
    #
    # Grouping of male
    for i in range(size_lst_set_country_code):
        for j in range(len(male_lst)):
            if lst_set_country_code[i] == male_lst[j][2]:
                lst_M[i].append(male_lst[j][2])
    # Grouping of female
    for i in range(size_lst_set_country_code):
        for j in range(len(female_lst)):
            if lst_set_country_code[i] == female_lst[j][2]:
                lst_F[i].append(female_lst[j][2]) 
    #            
    #Counting            
    male_count_by_city = [[lst_set_country_code[i],'Male',len(lst_M[i])] for i in range(size_lst_set_country_code)]         
    female_count_by_city = [[lst_set_country_code[i],'Female',len(lst_F[i])] for i in range(size_lst_set_country_code)]  
    #
    # Grouping both genders
    lst_lst = [[] for i in range(2*size_lst_set_country_code)] #Inicialization
    #
    for j in range(2*size_lst_set_country_code):
        if j % 2 == 0:
            k = int(j/2)
            lst_lst[j].append(male_count_by_city[k][0])
            lst_lst[j].append(male_count_by_city[k][1])
            lst_lst[j].append(male_count_by_city[k][2])            
        else:
            k = int((j-1)/2)
            lst_lst[j].append(female_count_by_city[k][0])
            lst_lst[j].append(female_count_by_city[k][1])
            lst_lst[j].append(female_count_by_city[k][2])
            
    #Table
    colnames_2 = ['country_code','gender','amount']
    genders_df = pd.DataFrame(lst_lst, columns=colnames_2)
    #
    return genders_df 


def Analisis_2(merge_df):
    #listing
    lst_gender = list(merge_df['gender'])
    lst_country_code = list(merge_df['country_code'])
    lst_normalized_job_code = list(merge_df['normalized_job_code'])
    #Set
    set_country_code = set(merge_df['country_code'])
    set_normalized_job_code = set(merge_df['normalized_job_code'])
    #
    # Listing Set
    lst_set_country_code = list(set_country_code)
    lst_set_normalized_job_code = list(set_normalized_job_code)
    #Size
    size_lst_gender = len(lst_gender)
    size_lst_set_country_code = len(lst_set_country_code)
    size_lst_set_normalized_job_code = len(lst_set_normalized_job_code)
    #
    #Listing genders
    female_lst = [[i,lst_gender[i],lst_country_code[i],lst_normalized_job_code[i]] for i in range(size_lst_gender) if lst_gender[i][0] == 'f' or lst_gender[i][0] == 'F']
    male_lst = [[i,lst_gender[i],lst_country_code[i],lst_normalized_job_code[i]] for i in range(size_lst_gender) if lst_gender[i][0] == 'm' or lst_gender[i][0] == 'M']
    #
    #initialization Grouping by country
    lst_M = [[] for i in range(size_lst_set_country_code)] 
    lst_F = [[] for i in range(size_lst_set_country_code)]
    #
    # Grouping of male by country
    for i in range(size_lst_set_country_code):
        for j in range(len(male_lst)):
            if lst_set_country_code[i] == male_lst[j][2]:
                #lst_M[i].append(male_lst[j][2])
                lst_M[i].append(male_lst[j][3])
    # Grouping of female by country
    for i in range(size_lst_set_country_code):
        for j in range(len(female_lst)):
            if lst_set_country_code[i] == female_lst[j][2]:
            # lst_F[i].append(female_lst[j][2]) 
                lst_F[i].append(female_lst[j][3])
    #            
    #set of jobs in each country            
    set_lst_M = [list(set(i)) for i in lst_M]
    set_lst_F = [list(set(i)) for i in lst_F]
    #
    #Grouping by jobs in each country
    lst_M_jobs = [[[k for k in lst_M[i] if k == j]for j in set_lst_M[i]] for i in range(size_lst_set_country_code)] 
    lst_F_jobs = [[[k for k in lst_F[i] if k == j]for j in set_lst_F[i]] for i in range(size_lst_set_country_code)]
    #
    # Size of grouping by jobs in each country
    M = len(lst_M_jobs)
    F = len(lst_F_jobs)
    #       
    #Counting            
    male_count_by_jobs_in_city = [[[lst_set_country_code[i],'Male',len(lst_M_jobs[i][j]),set_lst_M[i][j]]for j in range(len(lst_M_jobs[i]))]for i in range(M)]         
    female_count_by_jobs_in_city =[[[lst_set_country_code[i],'Female',len(lst_F_jobs[i][j]),set_lst_F[i][j]]for j in range(len(lst_F_jobs[i]))]for i in range(F)]  
    #
    # Reduce dimention
    m_c_b_j_c = [j for i in male_count_by_jobs_in_city for j in i]
    f_c_b_j_c = [j for i in female_count_by_jobs_in_city for j in i]
    #
    # Grouping both genders
    #lst_lst = [[] for i in range(len(m_c_b_j_c) + len(f_c_b_j_c))] #Inicialization
    #
    lst_lst = m_c_b_j_c + f_c_b_j_c
    #Table
    colnames = ['country_code','gender','amount_of_people','job_code']
    genders_df = pd.DataFrame(lst_lst, columns=colnames)
    #
    return  genders_df        #.groupby('gender')  
