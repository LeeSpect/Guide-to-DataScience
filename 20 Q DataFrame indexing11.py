# 2016년도에 KBS방송국의 시청률을 찾아봅시다.

import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)

df.loc[2016, 'KBS']  # 2016은 자료형이 숫자형이기 때문에 ''를 붙이지 않는다.
# --------------------------------------------------------------------------------------------------------------
#27.583000000000002