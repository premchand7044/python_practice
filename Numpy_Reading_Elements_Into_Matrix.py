import numpy as np
r = int(input("enter row size:"))
c = int(input("enter col size:"))
matrix = np.ndarray(shape=(r,c),dtype=int)
print("Enter %d elements of %dX%d matrix:" %(r*c ,r,c))
for i in range(r):
    for j in range(c):
        matrix[i][j]=int(input())
print("%dx%d matrix is:"%(r,c))
print(matrix)

