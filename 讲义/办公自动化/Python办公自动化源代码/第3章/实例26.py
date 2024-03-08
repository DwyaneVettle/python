import pandas as pd

page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')
stu=pd.Series({'学号':21,'姓名':'李强','成绩':91})

students=page1.append(stu,ignore_index=True)   #追加一行数据

students.to_excel('d:/abc/342.xlsx')  
