import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
with open('/content/drive/MyDrive/Data-sets-qqpp/test1.txt', 'r') as file:
    lines = file.readlines()
    data = [line.strip().split() for line in lines]
x_values, y_values = zip(*[(float(x), float(y)) for x, y in data])
plt.plot(x_values, y_values)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Line Plot with Labels')
plt.show()
