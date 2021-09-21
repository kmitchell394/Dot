import pandas as pd

df1 = pd.read_csv("D:\\Dot\\Dot EDI\\Truck 1.csv", index_col=0)
df2 = pd.read_csv("D:\\Dot\\Dotcsv.csv", index_col=0)

df3 = pd.merge(df1, df2,on="DOT ITEM NUMBER", how='left')
#print(df3)

df3.to_csv("D:\\Dot\\Dot EDI\\Truck 1.csv", index=False)