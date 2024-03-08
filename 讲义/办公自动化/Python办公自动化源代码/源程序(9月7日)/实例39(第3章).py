import pandas as pd

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')
page1.rename(columns={"成绩":"期末成绩"},inplace=True)   #修改列标题

page1.to_excel('d:/abc/356.xlsx')  
















