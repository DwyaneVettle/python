import xlwings as xw

app=xw.App(visible=True,add_book=False)
exbo=app.books.open(r"d:\abc\2312.xls")
she=exbo.sheets["sheet2"]

fw=she.range("B2:D5")        #设置工作范围

print(fw.color)              #获取背景颜色
exbo.close()
app.quit()

