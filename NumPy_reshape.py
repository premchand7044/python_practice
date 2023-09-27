import numpy as np
my_list=(10,20,30,40,50,60,70,80)
arr = np.array(my_list)
print(arr)
arr1 = arr.reshape(2,2,2)
print(arr1)
print("size:",arr1.size)
print("shape:",arr1.shape)
print("dimension:",arr1.ndim)