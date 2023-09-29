import pandas as pd
import numpy as np
sd=pd.Series()
print(sd)#Empty Series
l=[10,20,30,40,50]
sd=pd.Series(l)
print(sd)#Series using list
sd=pd.Series(l,index=['a','b','c','d','e'])
print(sd)#indexing
a=np.array(l)
print(a)
sa=pd.Series(a)
print(sa)#Series using array
d={'a':10,'b':20,'c':30}
print(pd.Series(d))#Series using dictionary
dt=[('a',10),('b',20),('c',30)]
print(pd.Series(dt))#series using list of tuples