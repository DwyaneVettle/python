import matplotlib.pyplot as plt
import matplotlib.style as ms
plt.plot([1, 2, 3], [3, 4, 5])
plt.text(1.9, 3.75, 'y+x+2', bbox=dict(facecolor='y'),
         family='serif', fontsize=18, fontstyle='normal',
         rotation=-60)
ms.use('seaborn-dark')
plt.show()
