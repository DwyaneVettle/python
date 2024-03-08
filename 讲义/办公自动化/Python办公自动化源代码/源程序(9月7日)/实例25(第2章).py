import xlwings as xw

app=xw.App(visible=True,add_book=False)
exbo=app.books.open(r"d:\abc\饮料销售情况.xls")
she=exbo.sheets["sheet1"]

fw=she.range("B2:F10")                #设置工作范围

fw.api.Borders(7).LineStyle=2         #左边框
fw.api.Borders(7).Weight=3
fw.api.Borders(8).LineStyle=2         #上边框
fw.api.Borders(8).Weight=3
fw.api.Borders(9).LineStyle=2         #下边框
fw.api.Borders(9).Weight=3
fw.api.Borders(10).LineStyle=2        #右边框
fw.api.Borders(10).Weight=3
fw.api.Borders(11).LineStyle=2        #内部垂直边框
fw.api.Borders(11).Weight=3
fw.api.Borders(12).LineStyle=2        #内部水平边框
fw.api.Borders(12).Weight=3

exbo.save(r"d:\abc\238.xls")          #保存工作簿
exbo.close()
app.quit()

