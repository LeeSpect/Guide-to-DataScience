import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]

my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'english_score', 'math_score'], index=['a', 'b', 'c', 'd'])
my_df
#       name   english_score   math_score
#0  dongwook              50           86
#1    sineui              89           31
#2   ikjoong              68           91
#3   yoonsoo              88           75

type(my_df)
#pandas.core.frame.DataFrame

my_df.columns
#Index(['name', 'english_score', 'math_score'], dtype='object')  # object는 pandas에서의 문자열

my_df.index
#Index(['a', 'b', 'c', 'd'], dtype='object')

my_df.dtypes
#name             object
#english_score     int64
#math_score        int64
#dtype: object
