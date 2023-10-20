import pandas as pd
data = {
    'Column1': ['apple', 'banana', 'cherry', 'date', 'elderberry'],
    'Column2': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)
substring = 'an'
indices = df['Column1'].str.find(substring)
df['Index_of_Substring'] = indices
print(df)
