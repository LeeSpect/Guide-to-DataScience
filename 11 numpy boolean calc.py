import numpy as np

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

array1 > 4
#array([False, False,  True,  True,  True,  True,  True,  True,  True, True,  True])

array1 % 2 == 0  # 짝수 판별
#array([ True, False, False, False, False, False, False, False, False,
#       False, False])

booleans = np.array([True, True, False, True, True, False, True, True, True, False, True])
np.where(booleans)  # True가 들어가 있는 인덱스만 출력
#(array([ 0,  1,  3,  4,  6,  7,  8, 10],)
---------------------------------------------------------------------------------------------------
# 위의 두 논리 결합
np.where(array1 > 4)
#(array([ 2,  3,  4,  5,  6,  7,  8,  9, 10], dtype=int64),)

filter = np.where(array1 > 4)
filter  # 4보다 큰 요소의 인덱스 값을 가지는 array
#(array([ 2,  3,  4,  5,  6,  7,  8,  9, 10], dtype=int64),)

array1[filter]  # 4보다 큰 값을 가지는 array
#array([ 5,  7, 11, 13, 17, 19, 23, 29, 31])
