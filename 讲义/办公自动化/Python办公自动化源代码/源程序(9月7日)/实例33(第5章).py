from openpyxl import Workbook 
wb=Workbook()                     #创建工作簿
ws=wb.create_sheet("第5章")       #创建工作表
wb.save(r"d:\abc\563.xlsx")    #保存文件
