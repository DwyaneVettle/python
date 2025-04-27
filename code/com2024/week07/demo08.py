"""
    break语句用于结束当前循环，不再继续循环，通常和if条件语句配合使用
    # for-in循环
for ...in ...:
    ......
    if ...
      break
从键盘录入密码，最多录入3次，如果正确就结束循环
"""
# 当循环10次，第3次跳出循环
for i in range(0, 10):
    if i == 3:
        break
    print(i)

