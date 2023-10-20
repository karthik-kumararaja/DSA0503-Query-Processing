import pandas as pd
import numpy as np
df = pd.read_csv('/content/drive/MyDrive/Data-sets-qqpp/school.csv')
grouped = df.groupby(['school', 'class'])
for (school, class_), group in grouped:
    print(f"School: {school}, Class: {class_}")
    print(group)
    print("\n")
