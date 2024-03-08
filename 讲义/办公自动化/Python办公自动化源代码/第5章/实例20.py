import xlrd
import xlwt
from xlutils.copy import copy

workbook=xlrd.open_workbook(r'd:\abc\饮料销售情况.xls') 
sheet=workbook.sheets()[0]
row1=sheet.row_values(0)                   	#取出第1行
cols={str(i):row1[i] for i in range(0,len(row1))}  	#设置行索引
col4=sheet.col_values(3)                   	#取出第4列，
rows={str(i):col4[i] for i in range(0,len(col4))}  	#设置列索引

mtitle="容量"    
mname="500ml"   
rindex="".join([i for i in rows if rows[i]==mname])  	#获取行索引
cindex="".join([i for i in cols if cols[i]==mtitle]) 		#获取列索引

rindex=int(rindex)                              	#转换数据类型     
cindex=int(cindex)                             	#转换数据类型

old_excel=xlrd.open_workbook(r'd:\abc\饮料销售情况.xls') 
new_excel=copy(old_excel)                     	#复制文件
ws=new_excel.get_sheet(0)                      	#获取工作表 
ws.write(rindex,cindex, '修改内容')               	#写入（修改）数据

new_excel.save(r'd:\abc\535.xls')                  	#保存文件
