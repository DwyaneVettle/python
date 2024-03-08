import pandas as pd
stu=pd.read_csv('d:/abc/学生名单.csv',encoding='gbk',index_col='学号') #读入csv文件

stu.to_excel('d:/abc/331.xlsx')
