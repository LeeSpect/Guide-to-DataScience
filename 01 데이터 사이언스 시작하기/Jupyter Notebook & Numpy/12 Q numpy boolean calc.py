# 20만 엔 이하의 매출만 담긴 numpy array를 출력해주세요.

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

revenue_in_yen_UP = np.array(revenue_in_yen)
filter = np.where(revenue_in_yen_UP <= 200000)
bad_days_revenue = revenue_in_yen_UP[filter]

#yen_array = np.array(revenue_in_yen)
#bad_days_revenue = yen_array[yen_array < 200000]

bad_days_revenue
--------------------------------------------------------------------------------------------------------------
#array([140000, 180000, 170000, 140000, 150000, 110000, 150000, 130000])
