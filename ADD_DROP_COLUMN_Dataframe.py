import pandas as pd
d =pd.read_excel("C:\\Users\\master\\Desktop\\gst.xlsx")
df =pd.DataFrame(d)
print(df)
df['GST']=0
print(df)
df['GST']=df['TOTAL']/15
print(df)