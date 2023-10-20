import pandas as pd
import numpy as np
df = pd.read_csv('/content/drive/MyDrive/Data-sets-qqpp/alcohol.csv')
dimensions = df.shape
print("Dimensions (Shape) of the DataFrame: ", dimensions)
column_names = df.columns
print("Column Names: ", column_names)
