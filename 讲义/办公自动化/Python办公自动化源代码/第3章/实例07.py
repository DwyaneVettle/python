import pandas as pd
books=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='饮料全表') 
books['总价']=books['单价']*books['数量']  	#计算

books.to_excel('d:/abc/317.xlsx')         	#保存位置
