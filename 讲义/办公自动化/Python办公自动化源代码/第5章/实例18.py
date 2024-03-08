import xlrd
import xlwt
from xlutils.copy import copy
old_excel = xlrd.open_workbook(r'd:\abc\饮料销售情况.xls')
new_excel = copy(old_excel)        	#复制工作表
ws = new_excel.get_sheet(0)        	#获取第1个工作表
ws.write(0, 0, '第1行,第1列')      	#写入数据
ws.write(0, 1, '第1行,第2列')
ws.write(0, 2, '第1行,第3列')
ws.write(1, 0, '第2行,第1列')
ws.write(1, 1, '第2行,第2列')
ws.write(1, 2, '第2行,第3列')
new_excel.save(r'd:\abc\533.xls')    	#保存文件
