import pandas as pd
data=pd.read_csv('/content/drive/MyDrive/Data-sets-qqpp/customer_id.csv')
missing_values=data.fillna(0)
print(missing_values)
