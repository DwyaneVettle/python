import pandas as pd

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')
stu=pd.Series({'学号':6,'姓名':'吴伟','成绩':97})

page1.iloc[5]=stu           #替换整行数据

page1.to_excel('d:/abc/344.xlsx')  











