import matplotlib.pyplot as plt
import numpy as np
mm= [22, 30, 35, 35, 26]
mw = [25, 32, 30, 35, 29]
sdm = [4, 3, 4, 1, 5]
sdw = [3, 5, 2, 3, 3]
bar_width = 0.35
plt.bar(x, mm, bar_width, label='Men', color='green', yerr=sdm, capsize=5)
plt.bar(x, mw, bar_width, bottom=mm, label='Women', color='red', yerr=sdw, capsize=5)
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')
plt.legend()
plt.show()
