import numpy as np
my_list=[[10,20,30],[40,50,60],[70,80,90]]
matrix = np.array(my_list)
print(matrix)
x = matrix[0:3,0:3]
print(x)
y = matrix[0:2,0:3]
print(y)
z = matrix[0:3,0:2]
print(z)
b = matrix[1:3,1:3]
print(b)