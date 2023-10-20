import pandas as pd
import numpy as np
df = pd.read_csv('/content/drive/MyDrive/Data-sets-qqpp/school.csv')
result = df.groupby('school')['age'].agg(['mean', 'min', 'max'])
print(result)
