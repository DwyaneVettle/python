import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']    	#设置默认字体
plt.rcParams['axes.unicode_minus']=False  	#正常显示负号

stu=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name="销售情况",index_col="品名")

stu['1月销量'].plot.pie(fontsize=8,counterclock=False,startangle=-270) #绘制饼图 

plt.title("饮料销量情况图",fontsize=20,fontweight='bold')   	#加入标题
plt.ylabel('1月销量',fontsize=14,fontweight='bold')         	#重新设置列标题

plt.show()
