import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)
x=np.arange(5)
y=np.random.randn(5)

fig,ax=plt.subplots()
vert_bars=ax.bar(x,y,color='red',align='center')

for bar,height in zip(vert_bars,y):
    if height<0:
        bar.set(color='yellow',edgecolor='darkred',linewidth=2)

plt.show()









