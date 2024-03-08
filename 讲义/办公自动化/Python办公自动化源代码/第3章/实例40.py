import pandas as pd
import numpy as np
page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')

page1['学号']=page1['学号'].astype(float) 	#转换为浮点数
for i in range(3,7):                    	#将数据填充为空值
    page1['学号'].at[i]=np.nan

page1.dropna(inplace=True)           	#删除工作表中的空值

page1.to_excel('d:/abc/357.xlsx')
