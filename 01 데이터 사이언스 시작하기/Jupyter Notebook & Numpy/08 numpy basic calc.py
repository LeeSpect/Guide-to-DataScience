import numpy as np

array1 = np.arange(10)
array2 = np.arange(10, 20)

array1
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

array2
#array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

array1 * 2
#array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
#for i in range(len(array1)):
#    array[i] = 2* array1[1]  # 파이썬에서는 이렇게 함

array1 / 2
#array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])

array1 + 2
#array([ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

array1 ** 2
#array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81])

array1
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

array1 = array1 + 2
array1
#array([ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

array1 = np.arange(10)
array2 = np.arange(10, 20)

array1 + array2
#array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

array1 * array2
#array([  0,  11,  24,  39,  56,  75,  96, 119, 144, 171])

array1 / array2
#array([0.        , 0.09090909, 0.16666667, 0.23076923, 0.28571429,
#       0.33333333, 0.375     , 0.41176471, 0.44444444, 0.47368421])
