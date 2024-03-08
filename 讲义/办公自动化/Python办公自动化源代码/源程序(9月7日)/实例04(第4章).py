import pandas as pd
import matplotlib .pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']      #设置默认字体
plt.rcParams['axes.unicode_minus']=False        #正常显示负号

stu=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='饮料全表')

stu.sort_values(by='数量',inplace=True,ascending=False)    #排序
stu.plot.bar(x='品名',y=['数量','总价'])                       #建立柱型图
plt.title('饮料销售情况',fontsize=16,fontweight='bold')     #设置图表标题及字体字号
plt.xlabel('品名',fontweight='bold')                          #设置图表行标题          
plt.ylabel('数量/总价',fontweight='bold')                     #设置图表列标题
ax=plt.gca()
ax.set_xticklabels(stu['品名'],rotation=360)                 #旋转行标题

plt.show()




















