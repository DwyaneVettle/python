import xlwings as xw
app=xw.App(visible=True,add_book=False)     #启动Excel程序
wobo=app.books.open(r"d:\abc\饮料销售情况.xls")
sht=wobo.sheets["sheet1"]
wobo.sheets.add("销售情况")                     #增加工作表

wobo.save(r"d:\abc\2210.xls")                 #保存工作簿
wobo.close()                                      #关闭工作簿
app.quit()                                        #退出Excel程序
