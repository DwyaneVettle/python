import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']      #设置默认字体
plt.rcParams['axes.unicode_minus']=False        #正常显示负号

stu=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name="饮料全表")

fig,axes=plt.subplots(2,1)
data=pd.Series(list(stu['单价']),index=list(stu['品名']))
data.plot.bar(ax=axes[0],color='k',alpha=0.7,rot=0)

data.plot.barh(ax=axes[1],color='k',alpha=0.7)

plt.show()


















