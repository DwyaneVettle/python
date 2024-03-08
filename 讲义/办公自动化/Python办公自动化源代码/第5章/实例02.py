import xlrd
data = xlrd.open_workbook('d://abc//饮料销售情况.xls') 	#打开文件
sheet_name = data.sheet_names()[1]                 	#打开工作表
print(sheet_name)                                	#输出工作表名称
