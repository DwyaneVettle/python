from openpyxl import load_workbook
wb=load_workbook(r'd:\abc\例题锦集.xlsx') 	#打开工作簿
ws=wb["销售数量"]
print(ws.title)                          	#输出工作表名称
