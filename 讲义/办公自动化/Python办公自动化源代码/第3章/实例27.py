import pandas as pd

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')
page1.at[7,'姓名']='李密'   #修改姓名列的数据

page1.to_excel('d:/abc/343.xlsx')       #写入Excel文件中
