import pandas as pd
from datetime import date,timedelta

def mon(d,md):
    yd=md//12
    m=d.month+md%12
    if m!=12:
        yd+=m//12
        m=m%12
    return date(d.year+yd,m,d.day)

books=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='销售报表',\
                    dtype={'销售日期':str})    #打开工作簿

start=date(2018,1,1)
for i in books.index:
    books["销售日期"].at[i]=mon(start,i)

books.to_excel('d:/abc/3110.xlsx')           #保存位置
