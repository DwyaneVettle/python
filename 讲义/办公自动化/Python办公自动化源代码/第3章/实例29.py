import pandas as pd
page1=pd.read_excel('d:/abc/例题锦集.xlsx',sheet_name='优秀名单')

stu=pd.Series({'学号':101,'姓名':'吴伟','成绩':97})

pa1=page1[:3]                   	#进行切片操作（左闭右开）
pa2=page1[3:]                   	#进行切片操作（左开右闭）

students=pa1.append(stu,ignore_index=True).append(pa2).reset_index(drop=True)  	#进行组合

students.to_excel('d:/abc/345.xlsx')
