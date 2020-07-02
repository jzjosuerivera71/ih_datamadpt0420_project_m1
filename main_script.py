#import argparse
import pandas as pd
from p_acquisition import m_acquisition as ac
#from p_wrangling import m_wrangling as wr
#from p_analysis import m_analysis as an 
#from p_reporting import m_reporting as mre 

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

#def argument_parser():
#    return args

#def main(some_args):
#    print()



if __name__ == '__main__':
    x = list(ac.acquire('personal_info')['gender'])
    print(x)
