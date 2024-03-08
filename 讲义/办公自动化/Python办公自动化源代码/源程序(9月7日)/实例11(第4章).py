import pandas as pd
import matplotlib .pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']      #设置默认字体
plt.rcParams['axes.unicode_minus']=False        #正常显示负号

stu=pd.read_excel('D:/abc/例题锦集.xlsx',sheet_name="股票数据",index_col='股票名称')

stu.最高.plot.density()        #建立密度图

plt.show()

























