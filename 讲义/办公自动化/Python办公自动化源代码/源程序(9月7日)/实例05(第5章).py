import xlrd
data = xlrd.open_workbook('d://abc//饮料销售情况.xls')  #打开文件
sheet = data.sheet_by_name('sheet1')                  #打开工作表
print(sheet.cell(1,0).value)               #输出指定单元格的内容
print(sheet.cell_value(1,0))               #输出指定单元格的内容
print(sheet.row(1)[0].value)               #输出指定单元格的内容

