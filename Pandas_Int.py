import pandas as pd
my_list=[10,20,30,40]
a=pd.Series(my_list)
print(a)
d={'name':['prem','chand','morla'],'percentage':[90,85,77]}
print(pd.DataFrame(d))