import pandas as pd
import time

timestr = time.strftime("%m-%d-%y")

read_file = pd.read_csv (r"D:\\Dot\\Dot EDI\\Truck 1.csv")
read_file.sort_values(by=['PO NUMBER', 'CUSTOMER ITEM NUMBER'], inplace=True)
read_file.to_excel(r"\\server-md3\\shared documents\\Crystal Reports\\Keith\\Dot.xlsx", index=None, header=True)
read_file.to_excel(r"D:\\Dot\\Dot EDI\\Dot "+timestr+".xlsx", index=None, header=True)

