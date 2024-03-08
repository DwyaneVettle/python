import pandas as pd
stu=pd.read_csv('d:/abc/学生名单.tsv',sep='\t',encoding='gbk',index_col='学号') #读入tsv文件

stu.to_excel('d:/abc/332.xlsx')   #写入Excel文件中
