import matplotlib.style as ms
import matplotlib.pyplot as plt
# print(ms.available)
plt.plot([1, 2, 3], [3, 4, 5])
plt.text(1.9, 3.75, 'y+x+2', bbox=dict(facecolor='y'),
         family='serif', fontsize=20, fontstyle='normal',
         rotation=60)

# 设置风格use()
ms.use('_mpl-gallery-nogrid')
plt.show()
