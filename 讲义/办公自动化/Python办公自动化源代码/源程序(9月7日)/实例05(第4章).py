import pandas as pd
import matplotlib .pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']      #设置默认字体
plt.rcParams['axes.unicode_minus']=False        #正常显示负号

stu=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name="销售情况")

stu.plot.barh(y=['1月销量','2月销量','3月销量','4月销量'],stacked=True) #建立柱形图
                          
plt.title("饮料销量情况图",fontsize=16,fontweight='bold')   #建立图表标题
plt.ylabel("数量",fontsize=12,fontweight='bold')            #设置图表Y轴
ax=plt.gca()
ax.set_xticklabels(stu['品名'],rotation=360)                #旋转行标题 

plt.show()





















