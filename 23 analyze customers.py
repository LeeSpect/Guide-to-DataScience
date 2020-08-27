# samsong.csv 파일과 hyundee.csv 파일. 두 회사의 데이터를 활용해서, 사람들의 요일별 문화생활비를 분석합니다.

import pandas as pd

samsong_df = pd.read_csv('data/samsong.csv')
hyundee_df = pd.read_csv('data/hyundee.csv')

dict1 = {
    'day': samsong_df['요일'],
    'samsong': samsong_df['문화생활비'],
    'hyundee': hyundee_df['문화생활비']
}

df = pd.DataFrame(dict1)
df

#combined_df = pd.DataFrame({
#    'day': samsong_df['요일'], 
#    'samsong': samsong_df['문화생활비'], 
#    'hyundee': hyundee_df['문화생활비']
#})
#combined_df
# --------------------------------------------------------------------------------------------------------------
#	day	samsong	hyundee
#0	MON	4308	5339
#1	TUE	7644	3524
#2	WED	5674	5364
#3	THU	8621	9942
#4	FRI	23052	33511
#5	SAT	15330	19397
#6	SUN	19030	19925
