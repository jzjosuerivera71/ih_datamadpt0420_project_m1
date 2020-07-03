import argparse
import numpy as np
from p_acquisition import m_acquisition as ac
from p_wrangling import m_wrangling as wr
from p_analysis import m_analysis as an 
#from p_reporting import m_reporting as re 

#def argument_parser():
#    parser = argparse.ArgumentParser(description = 'Set chart type')
#    parser.add_argument("-b", "--bar", help="Produce a barplot", action="store_true")
#    parser.add_argument("-l", "--line", help="Produce a lineplot", action="store_true")
#    args = parser.parse_args()
#    return args

#def main(some_args):
#    data = mac.acquire()
#    filtered = mwr.wrangle(data, year)
#    results = man.analyze(filtered)
#    fig = mre.plotting_function(results, title, arguments)
#    mre.save_viz(fig, title)
#    print('========================= Pipeline is complete. You may find the results in the folder ./data/results =========================')

#if __name__ == '__main__':
#    year = int(input('Enter the year: '))
#    title = 'Top 10 Manufacturers by Fuel Efficiency ' + str(year)
#    arguments = argument_parser()
#    main(arguments)

#Mi argument_parser
 
def argument_parser():
	parser = argparse.ArgumentParser(description = 'Which table you #want?')
	parser.add_argument("-p","--path",type=str,help = 'specify table')
	args = parser.parse_args()
	return args
	
def main(args):
	df_2=ac.acquire('country_info')
	df_3=ac.acquire('personal_info')
	df_4=ac.acquire('career_info')
	Cl_df_4 = wr.Cleaning_Dataframe_1(df_4)
	merge_df=wr.Merge(df_2,df_3,df_4,Cl_df_4)
	if args == 'by_coutry':
		x=an.Analisis_1(merge_df)
		print(np.array(x))
	elif args == 'by_jobs':
		x=an.Analisis_2(merge_df)
		print(np.array(x))
		
#    print()

#Options: {'poll_info','country_info','personal_info','career_info'}

if __name__ == '__main__':
	args = argument_parser() 
	main(args)
