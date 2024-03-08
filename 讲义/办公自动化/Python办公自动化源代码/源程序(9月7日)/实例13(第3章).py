import pandas as pd
books=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='饮料全表') 
books.sort_values(by='单价',inplace=True)     #排序

books.to_excel('d:/abc/321.xlsx')             #保存位置



