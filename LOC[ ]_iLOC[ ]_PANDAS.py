import pandas as pd
d=pd.read_excel('C:\\Users\\master\\Desktop\\python_Pr\\sample.xlsx')
df=pd.DataFrame(d)
print(df)
print(df.loc[4])
print(df.loc[4,'Gender'])
print(df.loc[1:4,['First Name','Gender']])
print(df.loc[1:4,'First Name':'Country'])
print(df.iloc[0:4,1:5])
