import pandas as pd
data = {
    'Text_Column': ['Hello', 'wOrLd', 'Python', 'pAnDaS', 'DaTaFrAmE']
}
df = pd.DataFrame(data)
df['Text_Column'] = df['Text_Column'].str.swapcase()
print(df)
