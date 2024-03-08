import pandas as pd
import numpy as np

stu=pd.read_excel('D:/abc/例题锦集.xlsx',sheet_name="销售报表",index_col='序号')
stu['Year']=pd.DatetimeIndex(stu['销售日期']).year

pt1=stu.pivot_table(index='类别',columns='Year',values='销售数量',aggfunc=np.sum)

pt1.to_excel('d:/abc/466.xlsx')  #写入Excel文件中
