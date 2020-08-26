import numpy as np

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

array1[[1, 3, 4]]
#array([3, 7, 11])

array2 = np.array([2, 1, 3])

array1[array2]
#array([5, 3, 7])

array1[2:11:2]
#array([5, 11, 17, 23, 31])

array1[2:11:3]
#array([5, 13, 23])
