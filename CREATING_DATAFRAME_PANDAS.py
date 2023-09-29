import pandas as pd
d=pd.read_excel('C:\\Users\\master\\Desktop\\gst.xlsx')#Using excel
print(d)
df=pd.DataFrame(d)
print(df)
df1=pd.read_csv('C:\\Users\\master\\Desktop\\gst.csv')#using csv
df2=pd.DataFrame(df1)
print(df2)
e={'player':['rohit','gill','virat','surya'],'runs':[200,100,150,180],'mathces':[1,1,1,1]}
df3=pd.DataFrame(e)
print(df3)