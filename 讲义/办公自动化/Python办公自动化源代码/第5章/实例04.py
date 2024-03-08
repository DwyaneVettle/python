import xlrd
data = xlrd.open_workbook('d://abc//饮料销售情况.xls')  	#打开文件
sheet = data.sheet_by_name('sheet1')                  	#打开工作表
print(sheet.row_values(3))                          	#输出整行信息
print(sheet.col_values(3))                            	#输出整列信息
