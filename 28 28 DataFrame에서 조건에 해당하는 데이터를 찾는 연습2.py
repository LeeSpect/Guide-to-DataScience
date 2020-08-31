# SBS가 TV CHOSUN보다 더 시청률이 낮았던 시기의 데이터를 확인

import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)

df.loc[df['SBS'] < df['TV CHOSUN'], ['SBS', 'TV CHOSUN']]
# --------------------------------------------------------------------------------------------------------------
#	SBS	TV CHOSUN
#2014	9.108	9.440
#2015	9.099	9.940
#2016	8.669	9.829
#2017	8.661	8.886
