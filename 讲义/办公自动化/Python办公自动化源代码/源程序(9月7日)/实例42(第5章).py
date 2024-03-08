from openpyxl import load_workbook
wb=load_workbook(r'd:\abc\例题锦集.xlsx')  #打开工作簿
ws=wb["班级成绩"]

for row in ws.rows:                           #按行输出数据
    for cell in row:
        print(cell.value,end=";")
print()
print('*****************')
for column in ws.columns:                    #按列输出数据
    for cell in column:
        print(cell.value,end=";")
