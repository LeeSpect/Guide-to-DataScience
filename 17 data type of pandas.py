# pandas DataFrame에는 다양한 종류의 데이터를 담을 수 있습니다. 
# dtypes를 사용해서 각 column이 어떤 데이터 타입을 보관하는지 확인할 수 있습니다.

import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]

my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'english_score', 'math_score'], index=['a', 'b', 'c', 'd'])

print(my_df.dtypes)

#name             object
#english_score     int64
#math_score        int64
#dtype: object

# 위 경우 'name' column은 object라는 데이터 타입을 보관하고, 'english_score'와 'math_score' column은 int64라는 데이터 타입을 보관합니다.
# 한 column 내에서는 모든 값이 동일한 데이터 타입입니다.
# --------------------------------------------------------------------------------------------------------------
# pandas의 dtype들
# dtype	      설명
--------------------------
# int64	      정수
# float64     소수
# object	    텍스트
# bool	      불린(참과 거짓)
# datetime64	날짜와 시간
# category	  카테고리
