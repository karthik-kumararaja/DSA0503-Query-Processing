import pandas as pd
data=pd.read_csv('/content/drive/MyDrive/Data-sets-qqpp/school_data.csv')
grouped = data.groupby('school')
print(grouped)
print(type(grouped))
