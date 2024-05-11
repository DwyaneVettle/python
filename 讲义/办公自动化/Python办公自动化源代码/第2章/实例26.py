import xlwings as xw

app = xw.App(visible=True, add_book=False)
exbo = app.books.open(r"d:\abc\饮料销售情况.xls")
she = exbo.sheets["sheet1"]

fw = she.range("B2:F10")  # 设置工作范围
fw.column_width = 8  # 设置列宽
fw.row_height = 25  # 设置行高
fw.api.HorizontalAlignment = -4152  # 设置靠右
fw.api.VerticalAlignment = -4107  # 设置靠下

exbo.save(r"d:\abc\239.xls")  # 保存工作簿
exbo.close()
app.quit()
