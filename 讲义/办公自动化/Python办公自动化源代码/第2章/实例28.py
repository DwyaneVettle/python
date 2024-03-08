import xlwings as xw

app=xw.App(visible=True,add_book=False)
exbo=app.books.open(r"d:\abc\2310.xls")
she=exbo.sheets["Sheet2"]

fw=she.range("B2")          	#设置工作范围

fw.api.UnMerge()            	#拆分单元格

exbo.save(r"d:\abc\2311.xls")  	#保存工作簿

exbo.close()
app.quit()
