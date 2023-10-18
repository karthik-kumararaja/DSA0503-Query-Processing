import pandas as pd
import numpy as np
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
df.iloc[2, 1] = np.nan
df.iloc[5, 3] = np.nan
df.iloc[7, 0] = np.nan
def highlight_nan(val):
    return f'background-color: yellow' if pd.isna(val) else ''
styled_df = df.style.applymap(highlight_nan)
styled_df
