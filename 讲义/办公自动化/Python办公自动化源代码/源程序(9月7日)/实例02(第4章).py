import pandas as pd
import matplotlib .pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']      #设置默认字体
plt.rcParams['axes.unicode_minus']=False        #正常显示负号

stu=pd.read_excel('D:/abc/例题锦集.xlsx',sheet_name="销售额度")

stu.plot.scatter(x='月份',y='销售额')   #建立散点图

plt.show()



















