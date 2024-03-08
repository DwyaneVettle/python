import pandas as pd
import matplotlib .pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']      #设置默认字体
plt.rcParams['axes.unicode_minus']=False        #正常显示负号

stu=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name="销售情况",index_col="品名")

stu['1月销量'].plot.pie()        #建立饼图

plt.show()






















