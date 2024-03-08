import xlwings as xw
app=xw.App(visible=True,add_book=False)            #启动Excel程序
wobo=app.books.open(r"d:\abc\饮料销售情况.xls")     #获取工作簿
she=wobo.sheets[0]                                     #获取工作表
fw=she.range("A1:F10")                                 #设置范围
for i in fw.current_region.value:
    print(i)
wobo.close()                                             #关闭工作簿
app.quit()                                               #退出Excel程序
