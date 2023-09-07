import numpy as np
my_list = [10,20,30,40,50]
arr = np.array(my_list)
print(arr)
#properties of numpy
print("size:",arr.size)
print("Shape:",arr.shape)
print("dimension:",arr.ndim)
print("datatype:",arr.dtype)
#matrix
my_list1 = [[10,20,30],[40,50,60],[70,80,90]]
matrix= np.array(my_list1)
print(matrix)
print("size:",matrix.size)
print("Shape:",matrix.shape)
print("dimension:",matrix.ndim)
print("datatype:",matrix.dtype)
