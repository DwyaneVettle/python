import xlwings as xw
app=xw.App(visible=True,add_book=False)
wobo=app.books.open(r"d:\abc\饮料销售情况.xls")
sht=wobo.sheets[0]
fw=sht.range("B12")
fw.add_hyperlink("www.baidu.com","百度","链接到百度")

wobo.save(r"d:\abc\248.xls")        	#保存文件
wobo.close()                     	#关闭工作簿
app.quit()                       	#退出工作簿
