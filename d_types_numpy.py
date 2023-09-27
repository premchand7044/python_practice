import numpy as np
my_list=(10,20,30,40)
arr=np.array(my_list,)#dtype="f"
print(arr)
x=arr.astype("U")
print(x)
c = arr.copy()
print(c)
c[1]=100
print(c)
v =arr.view()
print(v)
v[1] = 100
print(arr)