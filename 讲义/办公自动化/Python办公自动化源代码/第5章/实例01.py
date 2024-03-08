import xlrd
data = xlrd.open_workbook('d://abc//饮料销售情况.xls') 	#打开文件
sheet_name = data.sheet_names()                   	#获取所有工作表名称
print(sheet_name)                               	#输出所有工作表名称
