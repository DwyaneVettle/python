import xlrd
from xlutils.copy import copy
workbook=xlrd.open_workbook(r'd:\abc\饮料销售情况.xls')  #打开工作簿

new_workbook=copy(workbook)     	#复制

new_workbook.save(r'd:\abc\531.xls') 	#保存工作簿
