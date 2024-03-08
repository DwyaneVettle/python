import xlrd
import xlwt
from xlutils.copy import copy

wosh=xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")
new=copy(wosh)              	#复制工作簿

new.save(r"d:\abc\2211.xls")    	#保存工作簿
