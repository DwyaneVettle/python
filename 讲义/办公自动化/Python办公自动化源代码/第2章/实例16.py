import xlwings as xw
app=xw.App(visible=True,add_book=False)   #启动Excel程序
wobo=app.books.open(r"d:\abc\饮料销售情况.xls")
she=wobo.sheets["Sheet2"]
she.activate()                	#设置活动表格

wobo.save(r"d:\abc\2212.xls")  	#保存工作簿
wobo.close()               	#关闭工作簿
app.quit()                  	#退出Excel程序
