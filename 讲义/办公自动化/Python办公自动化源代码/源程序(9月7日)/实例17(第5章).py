import xlrd
workbook = xlrd.open_workbook(r'd:\abc\饮料销售情况.xls')  #打开工作簿
sheets = workbook.sheet_names()                #获取所有工作表名称并形成列表元素
worksheet = workbook.sheet_by_name(sheets[0])           #获取第1个工作表
rows_old = worksheet.nrows                      #获取第1个工作表中数据的行数
print("工作表的列标签为：")
print(sheets)
print()
print("工作表的名称为：",end="")
print(sheets[0])
print()
print("工作表的行数为：",end="")
print(worksheet.nrows)
