import pandas as pd
import numpy as np

df = pd.read_csv("D:\\Dot\\Dot EDI\\Truck 1.csv")

df.drop(['CUSTOMER ITEM NUMBER'], axis=1, inplace=True)
df.rename(columns={'Modern #': 'CUSTOMER ITEM NUMBER'}, inplace=True)

df = df[['PO NUMBER', 'SSCC', 'QUANTITY ORDERED', 'QUANTITY SHIPPED', 'DOT ITEM NUMBER', 'CUSTOMER ITEM NUMBER', 'MFG NUMBER', 'ITEM DESCRIPTION', 'GTIN', 'PALLET LIC PLATE', 'UA UPC NUMBER']]

df = df.astype(str)

df.to_csv("D:\\Dot\\Dot EDI\\Truck 1.csv", index=False)


