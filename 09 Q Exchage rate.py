# 엔화 매출이 담겨 있는 파이썬 리스트가 주어졌습니다. 1엔에 10.08원이라고 가정하고, 원화 매출이 담긴 numpy array를 만들어 출력해 주세요.

import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

yen_array = np.array(revenue_in_yen)
won_array = yen_array * 10.08

won_array
---------------------------------------------------------------------------------------------------
#array([ 3024000.,  3427200.,  3225600.,  3628800.,  4435200.,  1411200.,
#        1814400.,  3427200.,  3326400.,  2923200.,  2822400.,  3830400.,
#        1713600.,  1411200.,  2318400.,  3931200.,  4032000.,  3528000.,
#        3830400.,  1512000.,  1108800.,  2419200.,  3830400.,  3830400.,
#        3427200.,  4233600.,  1512000.,  1310400.,  3628800.,  3225600.,
#        2520000.])
