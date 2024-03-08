import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']      #设置默认字体
plt.rcParams['axes.unicode_minus']=False        #正常显示负号

stu=pd.read_excel('d:\\abc\\例题锦集.xlsx',sheet_name="销售情况",index_col="品名") 

stu.plot.area(y=['1月销量','2月销量','3月销量'])  #建立叠加区域图

plt.title('月份销售情况',fontsize=16,fontweight='bold')
plt.ylabel('总量',fontsize=12,fontweight='bold')

plt.show()






























