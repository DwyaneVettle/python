import pandas as pd        	#调用库

pe=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='饮料全表')

print(pe.head(2))           	#显示前2行内容
print('=========================')
print(pe.tail(3))            	#显示后3行内容
