import pandas as pd
import matplotlib .pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']      #设置默认字体
plt.rcParams['axes.unicode_minus']=False        #正常显示负号

stu=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name="销售数量")

stu.plot.area(y=['农夫山泉','加多宝','可口可乐','红牛饮料'])    #建立拆线图

plt.title("饮料销量情况图",fontsize=16,fontweight='bold')     #加入标题
plt.xlabel("产品名称",fontsize=12,fontweight='bold')          #设置X轴
plt.ylabel("销售数量",fontsize=12,fontweight='bold')          #设置Y轴

plt.show()


























