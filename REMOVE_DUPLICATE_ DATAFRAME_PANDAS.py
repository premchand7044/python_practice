import pandas as pd
d=pd.read_excel('C:\\Users\\master\\Desktop\\sample.xlsx')
df=pd.DataFrame(d)
print(df)
print(df.duplicated())
print(df.drop_duplicates())