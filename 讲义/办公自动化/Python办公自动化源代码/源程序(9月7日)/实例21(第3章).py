import pandas as pd
import numpy as np
tsb=pd.read_excel("d:/abc/例题锦集.xlsx",'销售报表')

tsb['年份']=pd.DatetimeIndex(tsb['销售日期']).year   #提取年份

groups=tsb.groupby(['类别','年份'])                    #分组
s=groups['销售数量'].sum()                               #计算销售总额

pt2=pd.DataFrame({'销售总额':s})                        #合并(聚合)

pt2.to_excel('d:/abc/329.xlsx')








