"""
    输入两个数，判断大小
"""
num01 = int(input("请输入第一个数："))
num02 = int(input("请输入第二个数："))
if num01 > num02:
    print(f"第一个数{num01}大")
elif num01 < num02:
    print(f"第二个数{num02}大")
else:
    print("两个数相等")
