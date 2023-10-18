import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/Data-sets-qqpp/Sales_data.csv')
pivot_table = df.pivot_table(index=['Region', 'Manager', 'SalesMan'], values='Sale_amt', aggfunc='sum')
print(pivot_table)
