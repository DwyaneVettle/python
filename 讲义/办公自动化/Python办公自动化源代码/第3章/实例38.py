import pandas as pd

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')
page1.insert(2,column="年龄",value=25)       #插入列数据

page1.to_excel('d:/abc/355.xlsx')
