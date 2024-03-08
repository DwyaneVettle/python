import pandas as pd
import matplotlib .pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']      #设置默认字体
plt.rcParams['axes.unicode_minus']=False        #正常显示负号

stu=pd.read_excel('D:/abc/例题锦集.xlsx',sheet_name="服装销售")

stu.月销售额.plot.hist(bins=30)                          #建立直方图

plt.xticks(range(5,40,10),fontsize=8,rotation=90)  #设置X轴间隔

plt.show()
























