import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
stu=pd.read_excel('D:/abc/例题锦集.xlsx',sheet_name="销售报表")
plt.rcParams['font.sans-serif']=['SimHei']  #设置默认字体
plt.rcParams['axes.unicode_minus']=False    #解决显示问题

stu1=pd.DataFrame(stu['销售数量'])
stu1.plot.area(stacked=False);

plt.show()





























