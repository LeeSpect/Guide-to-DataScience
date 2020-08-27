# 이번에는 DataFrame에서 여러 줄을 찾는 연습을 해보겠습니다.
# SBS와 JTBC의 시청률만 확인하려면 어떻게 하면 될까요?

import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)

names = {
    'SBS': df['SBS'],
    'JTBC': df['JTBC']
}

new_df = pd.DataFrame(names, index = df.index)
new_df

#import pandas as pd

#df = pd.read_csv('data/broadcast.csv', index_col=0)
#df[['SBS', 'JTBC']]
# --------------------------------------------------------------------------------------------------------------
#	SBS	JTBC
#2011	11.173	7.380
#2012	11.408	7.878
#2013	9.673	7.810
#2014	9.108	7.490
#2015	9.099	7.267
#2016	8.669	7.727
#2017	8.661	9.453
