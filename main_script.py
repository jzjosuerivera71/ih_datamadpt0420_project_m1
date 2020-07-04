import argparse
import numpy as np
from p_acquisition import m_acquisition as ac
from p_wrangling import m_wrangling as wr
from p_analysis import m_analysis as an 
#from p_reporting import m_reporting as re 



 
#def argument_parser():
#	parser = argparse.ArgumentParser(description = 'Which table you #want?')
#	parser.add_argument("-p","--path",type=str,help = 'specify table')
#	args = parser.parse_args()
#	return args
	
def main(args):
	df_2=ac.acquire('country_info')
	df_3=ac.acquire('personal_info')
	df_4=ac.acquire('career_info')
	Cl_df_4 = wr.Cleaning_Dataframe_1(df_4)
	merge_df=wr.Merge(df_2,df_3,df_4,Cl_df_4)
	if args == 'by_coutry':
		x=an.Analisis_1(merge_df)
		y=wr.Translator_1(x)
		print(y)
	elif args == 'by_jobs':
		x=an.Analisis_2(merge_df)
		y=wr.Translator_1(x)
		print(y)
		


if __name__ == '__main__':
	#args = argument_parser()
	args = 'by_coutry' 
	main(args)
