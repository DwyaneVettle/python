import xlwings as xw

app=xw.App(visible=True,add_book=False)
exbo=app.books.open(r"d:\abc\饮料销售情况.xls")
she=exbo.sheets["sheet2"]

fw=she.range("B2:D5")              #设置工作范围
fw.api.Merge()                      #合并单元格

exbo.save(r"d:\abc\2310.xls")    #保存工作簿
exbo.close()
app.quit()
