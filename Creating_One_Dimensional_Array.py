import numpy as np
n = int(input("size"))
arr = np.ndarray(shape=(n),dtype=int)
print("enter %d ele:"%n)
for i in range(n):
    arr[i] = int(input())
print("elements:",arr)
 