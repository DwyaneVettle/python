import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

labels='一班','二班','三班','四班'
sizes=[15,30,45,10]

fig=plt.figure()
ax=fig.add_subplot(111)

ax.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True)
ax.axis('equal')

plt.show()











