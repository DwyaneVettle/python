import pandas as pd

books=pd.read_excel("d:/abc/例题锦集.xlsx",sheet_name='期末成绩')

temp=books[['语文','数学','英语']]        	#提取数据
row_mean=temp.mean(axis=1)          	#计算一行的平均分
books['平均分']=row_mean            	#将平均分写入“平均分”列

books.to_excel('d:/abc/3112.xlsx')       	#保存位置
