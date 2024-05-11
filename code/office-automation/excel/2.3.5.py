import xlrd
import xlwt
from xlutils.copy import copy

exbo = xlrd.open_workbook(r"d:\abc\饮料销售情况.xls")

nexbo = copy(exbo)  # 复制工作簿
nsht = nexbo.get_sheet(0)  # 打开新的工作表

style = xlwt.XFStyle()  # 初始化样式（第1步）

alignment = xlwt.Alignment()  # 创建对齐属性对象（第2步）

alignment.vert = xlwt.Alignment.VERT_TOP  # 进行设置（第3步）
alignment.horz = xlwt.Alignment.HORZ_RIGHT

style.alignment = alignment  # 将设置好的属性对象赋值给style对应的属性（第4步）
nsht.write(12, 1, "文字格式", style)  # 写入数据时使用style对象（第5步）

nexbo.save(r"d:\abc\235.xls")  # 保存工作簿
