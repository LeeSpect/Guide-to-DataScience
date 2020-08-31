import numpy as np


array1 = numpy.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

array1
#array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29, 31])

type(array1) 
#numpy.ndarray  # ndarray = n차원 배열

array1.shape  # shape는 numpy array의 모양을 알려줌
#(11,)

array2 = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

type(array2)
#numpy.ndarray

array2  #2차원 array
#array([[ 1,  2,  3,  4],
#       [ 5,  6,  7,  8],
#       [ 9, 10, 11, 12]])

array2.shape 
#(3, 4)  # 행이 3개고 열이 4개인 2차원 배열이라는 뜻 

array1.size 
#11  # numpy array에 몇개의 요소가 들어가있는지 알려줌

array2.size
#12

