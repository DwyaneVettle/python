import xlwt
workbook=xlwt.Workbook()                	#创建工作簿
worksheet=workbook.add_sheet('第5章')      	#创建工作表
worksheet.write(0,0,5)                     	#写入数据
worksheet.write(0,1,2)                      	#写入数据

worksheet.write(1,0,xlwt.Formula('A1*B1'))     	#写入公式
worksheet.write(1,1,xlwt.Formula('SUM(A1,B1)')) 	#写入公式

workbook.save(r'd:\abc\524.xls')              	#保存文件
