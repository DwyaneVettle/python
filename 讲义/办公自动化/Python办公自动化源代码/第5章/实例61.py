import matplotlib.pyplot as plt
import numpy as np
np.random.seed(20000101)

N=50
x=np.random.rand(N)
y=np.random.rand(N)
colors=np.random.rand(N)
area=(30*np.random.rand(N))**2  #散点半径

plt.scatter(x,y,s=area,c=colors,alpha=0.5)

plt.show()
