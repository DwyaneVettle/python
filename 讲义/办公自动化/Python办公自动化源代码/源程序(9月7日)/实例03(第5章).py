import xlrd
data = xlrd.open_workbook('d://abc//饮料销售情况.xls')  #打开文件
sheet= data.sheet_by_index(0)                           #打开工作表
print(sheet.name)                                         #输出sheet名称
print(sheet.nrows)                                        #输出sheet行数
print(sheet.ncols)                                        #输出sheet列数

