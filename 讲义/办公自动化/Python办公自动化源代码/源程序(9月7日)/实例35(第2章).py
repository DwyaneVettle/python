import xlwings as xw

app=xw.App(visible=True,add_book=False)
exbo=app.books.open(r"d:\abc\饮料销售情况.xls")
she=exbo.sheets["sheet1"]

fw=she.range("B2:D5")   #设置工作范围

print(fw.column)        #查找指定范围的列标
exbo.close()
app.quit()
