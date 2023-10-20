import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot([1, 2, 3], [3, 4, 5])
plt.text(1.9, 3.75, 'y+x+2', bbox=dict(facecolor='y'),
         family='serif', fontsize=18, fontstyle='normal',
         rotation=-60)
plt.show()
