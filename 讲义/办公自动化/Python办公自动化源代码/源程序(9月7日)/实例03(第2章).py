import xlrd
excelbook=xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")   #获取工作簿
she=excelbook.sheet_by_name("sheet1")                      #获取工作表
for i in range(she.nrows):                                 #输出工作表中的数据
    print(she.row(i))
