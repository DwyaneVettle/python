import pandas as pd
import numpy as np
tsb=pd.read_excel("d:/abc/例题锦集.xlsx",'销售报表')

tsb['年份']=pd.DatetimeIndex(tsb['销售日期']).year   #提取年份

tsb1=tsb.pivot_table(index='类别',columns='年份',values='销售数量',\
                     aggfunc=np.sum)                     #建立数据透视表

tsb1.to_excel('d:/abc/328.xlsx')  







