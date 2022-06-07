# author by Michealzou@126.com
# 2022/5/24 10:41
# else子句
num = input("请输入分页显示的数据条数：")
try:
    page_size = int(num)
except Exception as e:
    page_size = 20
    # 不符合输入要求，显示20页默认数据
    print(f"当前页显示{page_size}条数据")
else:
    # 符合要求，显示输入数字的页数
    print(f"当前页显示{num}条数据")