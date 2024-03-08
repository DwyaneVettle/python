import pandas as pd

def dj(x):                            	#定义单价筛选条件
    return  2<x<3

books=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='饮料全表')  
books=books.loc[books['单价'].apply(dj)]   	#以条件dj对单价进行筛选

books.to_excel('d:/abc/324.xlsx')         	#保存位置
