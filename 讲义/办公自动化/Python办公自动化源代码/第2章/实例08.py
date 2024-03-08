import xlrd
excelbook=xlrd.open_workbook(r"d:\abc\饮料销售情况.xls") 	#获取工作簿
she=excelbook.sheets()[0]                              	#获取工作表
print(she.row(2))  
