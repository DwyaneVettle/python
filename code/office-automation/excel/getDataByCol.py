import xlrd

excelbook = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")
she = excelbook.sheets()[0]
print(she.col(3))  # 获取工作表中第4列数据
