import pandas as pd
from pandas_profiling import ProfileReport
from pandas_profiling.utils.cache import cache_file

#Data:
#https://www.kaggle.com/datasets/whenamancodes/alcohol-effects-on-study?select=Maths.csv
#https://www.kaggle.com/datasets/whenamancodes/alcohol-effects-on-study?select=Portuguese.csv
#https://www.kaggle.com/datasets/sonukumari47/students-performance-in-exams
#Student_Performance_new.csv
#

data_file = input('Digite o nome do arquivo: ')

try:
    df = pd.read_csv(f'dados/{data_file}.csv', sep=',')
except:
    df = pd.read_csv(f'dados/{data_file}.csv', sep=';')

profile = ProfileReport(df, title=f"{data_file} Dataset")
profile.to_file(f"{data_file}.html")