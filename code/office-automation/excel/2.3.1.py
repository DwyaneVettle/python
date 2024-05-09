import xlrd
import xlwt
from xlutils.copy import copy
exbo = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")
nexbo = copy(exbo)                  	#复制工作簿
nsht = nexbo.get_sheet(0)              	#打开新的工作表
nsht.col(0).width = 256*20             	#设置列宽，256为一个衡量单位
nsht.row(0).height_mismatch=True     	#行高初始化
nsht.row(0).height = 20*40             	#设置行高，20为一个衡量单位

nexbo.save(r"d:\abc\231.xls")          	#保存工作簿
