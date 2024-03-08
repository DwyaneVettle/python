import xlwings as xw                                      #导入库
wb=xw.Book(r"d:\abc\饮料销售情况.xls")
sht=wb.sheets["sheet1"]
sht.range("A1").value=sht.range("A1").value+"名称"   #修改对应表格数据

wb.save(r"d:\abc\229.xls")                               #保存工作簿
