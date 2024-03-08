import pandas as pd

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')
page2=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='良好名单')

stu=pd.concat((page1,page2),axis=1)      #合并工作表

stu.to_excel('d:/abc/351.xlsx')
