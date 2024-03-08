import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']   	#设置默认字体
plt.rcParams['axes.unicode_minus']=False  	#正常显示负号

stu=pd.read_excel('D:/abc/例题锦集.xlsx',sheet_name="销售报表")

x=stu['品名']
y=stu['销售数量']
plt.pie(y,labels=x,autopct='%.2f%%',pctdistance=0.85,radius=1.0,labeldistance=1.1, \
wedgeprops={'width':0.3,'linewidth':2,'edgecolor':'white'})    #绘制环形图
plt.title(label='产品销售数量占比图',fontdict={'color':'black', 'size':20},loc='center')

plt.show()
