import xlrd
workbook=xlrd.open_workbook(r'd:\abc\饮料销售情况.xls') 
sheet1=workbook.sheets()[0]              	#打开工作表

col4=sheet1.col_values(3)                	#取出第4列
row={str(i):col4[i] for i in range(0,len(col4))} 	#设置行索引

row1=sheet1.row_values(0)                 	#取出第1行
col={str(i):row1[i] for i in range(0,len(row1))} 	#设置列索引

print("行索引内容为：",end=" ")
print(list(enumerate(row)))                 	#输出行索引
print("列索引内容为：",end=" ")
print(list(enumerate(col)))                 	#输出列索引

mtitle="容量"   
mname="500ml"   
a="".join([i for i in row if row[i]==mname]) 		#获取“容量”所在行索引
b="".join([i for i in col if col[i]==mtitle])			#获取500ml所在列索引
print("500ml的行索引与列索引分别为：",end=" ")
print(a,b)                               	#输出行索引和列索引
