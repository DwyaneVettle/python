import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']      #设置默认字体
plt.rcParams['axes.unicode_minus']=False        #正常显示负号

stu=pd.read_excel('D:/abc/例题锦集.xlsx',sheet_name="销售额度")

size=stu['销售额'].rank()  #先定义气泡大小
n=20                          #n 为倍数，用来调节气泡的大小 

plt.scatter(stu['月份'],stu['销售额'],s=size*n,alpha=0.6)   #建立气泡图

plt.show()




























