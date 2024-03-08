import pandas as pd
books=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='饮料全表')
books.sort_values(by=['容量','单价'],inplace=True,ascending=[True,False]) 

books.to_excel('d:/abc/323.xlsx')   #保存位置
