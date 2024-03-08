import xlrd
data = xlrd.open_workbook('d://abc//饮料销售情况.xls')  #打开文件
sheet = data.sheet_by_name('sheet1')                 #打开工作表
print(sheet.cell(1,0).ctype)             #输出单元格内容的数据类型
print(sheet.cell(3,4).ctype)             #输出单元格内容的数据类型
