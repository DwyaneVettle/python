import xlrd
excelbook = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")  # 获取工作簿
she = excelbook.sheet_by_index(0)  # 获取工作表
for i in range(she.nrows):
    print(she.row(i))  # 输出工作表内容