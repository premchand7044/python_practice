import numpy as np
my_list = [[10,20,30],[40,50,60],[70,80,90]]
matrix = np.array(my_list)
print(matrix)
matrix1 = matrix[0:3,0:3]
print(matrix1)
sub_matrix = matrix[0:2,0:2]
print(sub_matrix)
sub_matrix1 = matrix[1:3,1:3]
print(sub_matrix1)