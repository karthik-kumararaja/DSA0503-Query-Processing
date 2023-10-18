import pandas as pd
import numpy as np
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
def set_styles(val):
    return f'background-color: black; color: yellow;'
styled_df = df.style.applymap(set_styles)
styled_df
