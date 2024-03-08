import xlwings as xw

app=xw.App(visible=True,add_book=False)
exbo=app.books.open(r"d:\abc\2312.xls")
she=exbo.sheets["Sheet2"]

fw=she.range("B2:D5")         	#设置工作范围

fw.color=(255,255,255)        	#清除背景颜色

exbo.save(r"d:\abc\2314.xls")  	#保存工作簿
exbo.close()
app.quit()
