import pandas as pd
d=pd.read_excel("C:\\Users\\master\\Desktop\\python_Pr\\gst.xlsx")
df=pd.DataFrame(d)
print(df)
df['GST']=df['TOTAL']/15
print(df)
df.to_excel("C:\\Users\\master\\Desktop\gst1.xlsx",index=False)
df.to_csv("C:\\Users\\master\\Desktop\gst1.csv",index=False)
df.to_csv("C:\\Users\\master\\Desktop\gst1.txt",index=False,sep='\t')