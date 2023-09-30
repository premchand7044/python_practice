import pandas as pd
d=pd.read_excel("C:\\Users\\master\\Desktop\\sample.xlsx")
df=pd.DataFrame(d)
print(df)
print(df[1:8])
print(df[1:8:2])
print(df['First Name'][1:3])
print(df.loc[1])