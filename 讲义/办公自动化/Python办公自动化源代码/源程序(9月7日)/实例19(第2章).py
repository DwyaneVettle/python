import xlrd
import xlwt
from xlutils.copy import copy
exbo=xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")
nexbo=copy(exbo)                                #复制工作簿
nsht=nexbo.get_sheet(0)                        #打开新的工作表

style=xlwt.XFStyle()                           #初始化样式(第1步)
font=xlwt.Font()                               #创建属性对象(第2步)

font.name="黑体"                                #设置字体名称(第3步)
font.blod=False                                #是否加粗
font.height=400                                #设置字号，字号*20

style.font=font        #将设置好的属性赋值给style的对应的属性(第4步)
nsht.write(12,1,"文字格式",style)    #写入数据时使用style对象(第5步)

nexbo.save(r"d:\abc\232.xls")                  #保存工作簿

