import numpy as np
my_list =(60,50,30,40,20,10,30)
arr=np.array(my_list)
print(arr)
a = np.sort(arr)
print(a)
my_list1 = ((60,50,40),(30,20,10))
b = np.array(my_list1)
print(b)
c = np.sort(b)
print(c)
d = np.sort(b,axis=0)
print(d)
e= np.dtype([('name','S10'),('perc',float)])
stud = np.array([('abc',90.6),('def',85.6),('ghi',88.4)],dtype=e)
print(stud)
f = np.sort(stud,order='perc')
print(f)