import pandas as pd
from datetime import date,timedelta
books=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='销售报表',\
                    dtype={'销售日期':str})   #打开工作簿

start=date(2018,1,1)
for i in books.index:
    books["销售日期"].at[i]=start+timedelta(days=i)

books.to_excel('d:/abc/318.xlsx')            #保存位置
