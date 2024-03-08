import pandas as pd      #调用库

pe=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='饮料全表')

print(pe.shape)          #测试总行数及总列数
print(pe.columns)        #显示行的名称

print(pe.head())         #显示其内容
