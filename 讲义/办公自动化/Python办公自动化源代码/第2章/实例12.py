import xlwings as xw                	#导入库
wb=xw.Book(r"d:\abc\饮料销售情况.xls")
sht=wb.sheets["sheet1"]
sht.range("A3").value="百事可乐"     	#修改对应表格数据   

wb.save(r"d:\abc\228.xls")            	#保存工作簿
