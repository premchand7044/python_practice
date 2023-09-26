import numpy as np
arr = np.ndarray(shape=(4,4,4,4), dtype=int)
val = 1
x = arr.shape[0]
y = arr.shape[1]
z = arr.shape[2]
p = arr.shape[3]
for i in range(x):
    for j in range(y):
        for k in range(z):
            for l in range(p):
                arr[i][j][k][l] = val
                val =  val+1
print(arr)



