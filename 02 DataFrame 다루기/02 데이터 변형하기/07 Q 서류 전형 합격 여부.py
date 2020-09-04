# 각 파트가 최소 250점, 총 점수가 최소 600점이 되어야 서류 전형을 합격할 수 있습니다.
# 기존 DataFrame에 “합격 여부”라는 column을 추가하고, 합격한 지원자는 불린 값 True, 불합격한 지원자는 불린 값 False를 넣어주면 됩니다.

import pandas as pd
    
df = pd.read_csv('data/toeic.csv')

df['합격 여부'] = 'False'

condition = (df['LC']>=250) & (df['RC']>=250) & ((df['RC']+df['LC'])>=600)
df.loc[condition, '합격 여부'] = 'True'

df
'''
------------------------------------------------------------
import pandas as pd

df = pd.read_csv('data/toeic.csv')

pass_total = df['LC'] + df['RC'] > 600
pass_both = (df['LC'] >= 250) & (df['RC'] >= 250)
df['합격 여부'] = pass_total & pass_both

# 정답 출력
df
------------------------------------------------------------
'''
'''
--------------------------------------------------------------------------------------------------------------
	Gender	LC	RC	합격 여부
0	female	315	320	True
1	female	430	245	False
2	female	430	475	True
3	male	180	220	False
4	male	325	350	True
5	female	295	400	True
6	female	405	475	True
7	male	155	150	False
8	male	280	315	False
9	female	215	475	False
--------------------------------------------------------------------------------------------------------------
'''
