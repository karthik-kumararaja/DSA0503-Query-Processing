import pandas as pd
df=pd.read_csv('/content/drive/MyDrive/Data-sets-qqpp/purchase_data.csv')
nan_values = df.isna().sum(axis=1)
df = df[nan_values >= 2]
print(df)
