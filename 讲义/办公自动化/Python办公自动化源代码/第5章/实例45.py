from openpyxl import load_workbook
wb=load_workbook(r'd:\abc\例题锦集.xlsx')  	#打开工作簿
ws=wb["饮料简介"]

ws.sheet_properties.tabColor = "9c0006"     	#设置工作表标签颜色

wb.save(r"d:\abc\5615.xlsx")               	#保存文件
