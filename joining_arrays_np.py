import numpy as np
arr1 =np.arange(6).reshape(2,3)
print(arr1)
arr2 = np.arange(7,13).reshape(2,3)
print(arr2)
a =np.concatenate((arr1,arr2))
print(a)
b = np.concatenate((arr1,arr2),axis=1)
print(b)
c = np.stack((arr1,arr2))
print(c)
d= np.vstack((arr1,arr2))
print(d)
e = np.hstack((arr1,arr2))
print(e)
f = np.dstack((arr1,arr2))
print(f)