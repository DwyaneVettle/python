import xlwings as xw

app=xw.App(visible=True,add_book=False)
exbo=app.books.open(r"d:\abc\饮料销售情况.xls")
she=exbo.sheets["sheet1"]

fw=she.range("B2:D5")         #设置工作范围

print(fw.columns)              #查找指定范围的“范围”
print(len(fw.columns))        #测试指定范围列的个数 
print(fw.columns(1).value)   #输出指定范围内第1列的数据

exbo.close()
app.quit()
