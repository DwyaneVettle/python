import pandas as pd
stu=pd.read_table('d:/abc/学生名单.txt',encoding='gbk',index_col='学号') #读入txt文件

stu.to_excel('d:/abc/333.xlsx')  
