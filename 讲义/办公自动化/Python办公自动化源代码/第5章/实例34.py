from openpyxl import Workbook 
wb=Workbook()                	#创建工作簿
ws2=wb.create_sheet("第5章", 0)  	#创建工作表
wb.save(r"d:\abc\564.xlsx")      	#保存文件
