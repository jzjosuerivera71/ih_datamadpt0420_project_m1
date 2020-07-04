import pandas as pd
import requests
from bs4 import BeautifulSoup
#import re
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



grou=[['BE', 'Belgium'], ['EL', 'Greece'], ['LT', 'Lithuania'], ['PT', 'Portugal'], ['BG', 'Bulgaria'], ['ES', 'Spain'], ['LU', 'Luxembourg'], ['RO', 'Romania'], ['CZ', 'Czechia'], ['FR', 'France'], ['HU', 'Hungary'], ['SI', 'Slovenia'], ['DK', 'Denmark'], ['HR', 'Croatia'], ['MT', 'Malta'], ['SK', 'Slovakia'], ['DE', 'Germany'], ['IT', 'Italy'], ['NL', 'Netherlands'], ['FI', 'Finland'], ['EE', 'Estonia'], ['CY', 'Cyprus'], ['AT', 'Austria'], ['SE', 'Sweden'], ['IE', 'Ireland'], ['LV', 'Latvia'], ['PL', 'Poland'], ['UK', 'UnitedKingdom'], ['IS', 'Iceland'], ['NO', 'Norway'], ['LI', 'Liechtenstein'], ['CH', 'Switzerland'], ['ME', 'Montenegro'], ['MK', 'NorthMacedonia'], ['AL', 'Albania'], ['RS', 'Serbia'], ['TR', 'Turkey'], ['BA', 'BosniaandHerzegovina'], ['XK', 'Kosovo'], ['AM', 'Armenia'], ['BY', 'Belarus'], ['GE', 'Georgia'], ['AZ', 'Azerbaijan'], ['MD', 'Moldova'], ['UA', 'Ukraine'], ['DZ', 'Algeria'], ['LB', 'Lebanon'], ['SY', 'Syria'], ['EG', 'Egypt'], ['LY', 'Libya'], ['TN', 'Tunisia'], ['IL', 'Israel'], ['MA', 'Morocco'], ['JO', 'Jordan'], ['PS', 'Palestine'], ['RU', 'Russia'], ['AR', 'Argentina'], ['CN_X_HK', 'China'], ['MX', 'Mexico'], ['ZA', 'SouthAfrica'], ['AU', 'Australia'], ['HK', 'HongKong'], ['NG', 'Nigeria'], ['KR', 'SouthKorea'], ['BR', 'Brazil'], ['IN', 'India'], ['NZ', 'NewZealand'], ['TW', 'Taiwan'], ['CA', 'Canada'], ['JP', 'Japan'], ['SG', 'Singapore'], ['US', 'UnitedStates']]
    
    
def Translator_1(analisis_df):
	lst_country_code = list(analisis_df['country_code'])
	# web-scraping
	#url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
	#html = requests.get(url).content
	#soup = BeautifulSoup(html, 'lxml')
	#table = soup.find('div',id = 'mw-content-text')
	#rows = table.find_all('tr')
	#rows_lst = [row for row in rows]
	#rows_lst_2 = [str(i) for i in rows_lst]
	#
	#regex sub for cleaning
	#rows_lst_3 = [re.sub('<tr>','',i) for i in rows_lst_2]
	#rows_lst_4 = [re.sub('\n','',i) for i in rows_lst_3]
	#rows_lst_5 = [re.sub('<td>','',i) for i in rows_lst_4]
	#rows_lst_6 = [re.sub('</td>','',i) for i in rows_lst_5]
	#rows_lst_7 = [re.sub('</tr>','',i) for i in rows_lst_6]
	#rows_lst_8 = [re.sub('</a>','',i) for i in rows_lst_7]
	#rows_lst_9 = [re.sub('\xa0','',i) for i in rows_lst_8]
	#rows_lst_10 = [re.sub('<sup class="reference" id="cite_ref-3">','',i) for i in rows_lst_9]
	#rows_lst_11 = [re.sub('<sup class="reference" id="cite_ref-2">','',i) for i in rows_lst_10]
	#rows_lst_12 = [re.sub('<a href="#cite_note-2">','',i) for i in rows_lst_11]
	#rows_lst_13 = [re.sub('</sup>','',i) for i in rows_lst_12]
	#rows_lst_14 = [re.sub('<sup class="reference" id="cite_ref-1">','',i) for i in rows_lst_13]
	#rows_lst_15 = [re.sub('<a href="#cite_note-1">','',i) for i in rows_lst_14]
	#rows_lst_16 = [re.sub('[1]','',i) for i in rows_lst_15]
	#rows_lst_17 =[re.sub('[2]','',i) for i in rows_lst_16]
	#rows_lst_18 =[re.sub('[3]','',i) for i in rows_lst_17]
	#rows_lst_19 =[re.sub('<a href="#cite_note-">','',i) for i in rows_lst_18]
	#rows_lst_20 =[re.sub(' ','',i) for i in rows_lst_19]
	#
	#Split for cleaning
	#split_lst_1 = [i.split('(') for i in rows_lst_20]
	#low_dim_1 = [j for i in split_lst_1 for j in i]
	#split_lst_2 = [i.split(')') for i in low_dim_1]
	#low_dim_2 = [j for i in split_lst_2 for j in i]
	#clening_1 = [i for i in low_dim_2 if i != '']
	#clening_2 = [i for i in clening_1 if i != 'exceptHongKong']
	#clening_3 = []
	#
	#for i in clening_2:
	#    if i == 'Kosovo*[]':
	#        clening_3.append('Kosovo')
	#    else:
	#        clening_3.append(i)
	#
	#clening_4 = []
	#for i in clening_3:
	#    if i == 'XK[]':
	#        clening_4.append('XK')
	#    else:
	#        clening_4.append(i) 
	#        
	#clening_5 = []
	#for i in clening_4:
	#    if i == 'Palestine*[]':
	#        clening_5.append('Palestine')
	#    else:
	#        clening_5.append(i)
	#creo que me faleta un filtro para china
	#Grouping:
	#
	#lst_code = [clening_5[i] for i in range(len(clening_5)) if (i % 2) != 0 ]
	#lst_country = [clening_5[i] for i in range(len(clening_5)) if (i % 2) == 0]
	#
	#grou = [[] for i in range(int(len(clening_5)/2))] #initialization
	#
	#for i in range(len(grou)):
	#    grou[i].append(lst_code[i])
	#    grou[i].append(lst_country[i])
	#    
	#exchange
	new_lst = []
	for i in lst_country_code:
		for j in range(len(grou)):
			if i == grou[j][0]:
				new_lst.append(grou[j][1])
    	#
    	# Prepare data for Dataframe
	if len(list(analisis_df)) == 3:
		lst_1_1= list(analisis_df['gender'])
		lst_2_1= list(analisis_df['amount'])
		lst_lst_1 = [[new_lst[i],lst_1_1[i],lst_2_1[i]] for i in range(len(new_lst))]
		colnames_1 = ['country','gender','amount_of_people_by_country']
		new_genders_df_1 = pd.DataFrame(lst_lst_1, columns=colnames_1)
		return new_genders_df_1
	elif len(list(analisis_df)) == 4:
		lst_1_2= list(analisis_df['gender'])
		lst_2_2= list(analisis_df['amount_of_people'])
		lst_3_2= list(analisis_df['job_code'])
		lst_lst_2 = [[new_lst[i],lst_1_2[i],lst_2_2[i],lst_3_2[i]] for i in range(len(new_lst))] 
		colnames_2=['country','gender','amount_of_people_by_jobs','job_code']			
		new_genders_df_2 = pd.DataFrame(lst_lst_2, columns=colnames_2)
		return new_genders_df_2    

           
