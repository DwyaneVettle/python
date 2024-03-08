import xlwt

wb = xlwt.Workbook()  # 创建新的工作簿
she = wb.add_sheet("销售情况")  # 创建新的工作表
she.write(0, 0, "品名")  # 写入数据
she.write(0, 1, "编号")  # 写入数据
wb.save(r"d:\abc\221.xls")  # 保存工作簿
