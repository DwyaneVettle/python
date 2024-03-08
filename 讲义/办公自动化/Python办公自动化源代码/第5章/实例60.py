import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

bj='一班','二班','三班','四班'
rs=[15,30,45,10]

fig=plt.figure()
ax=fig.add_subplot(111)

ax.pie(rs,labels=bj,autopct='%1.1f%%',shadow=True)

plt.show()
