import pandas as pd

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')
page2=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='良好名单')

stu=page1.append(page2).reset_index(drop=True)   #合并

stu.to_excel('d:/abc/341.xlsx')









