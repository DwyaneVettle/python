import xlwings as xw

app=xw.App(visible=True,add_book=False)
exbo=app.books.open(r"d:\abc\饮料销售情况.xls")
she=exbo.sheets["sheet1"]

fw=she.range("A1:F10")                #设置工作范围
def zh(r,g,b):                          #转换函数
    return (2**16)*b+(2**8)*g*r

fw.api.Font.Color=zh(12,56,122)     #设置颜色

exbo.save(r"d:\abc\237.xls")         #保存工作簿


