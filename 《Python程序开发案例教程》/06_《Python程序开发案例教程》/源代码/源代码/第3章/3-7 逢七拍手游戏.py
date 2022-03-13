# 包含7和7的倍数小游戏（100以内）
for i in range(1, 101):
    # 把i转成字符串，使用find方法（字符串中不包含时，返回-1）
    include = str(i).find("7")
    # 判断条件：既不包含7，也不是7的倍数
    if include == -1 and int(i) % 7 != 0:
        # 输出，去掉了换行符，加了、
        print(i, end="、")
        # 如果包含7 输出*
    elif include != -1 or int(i) % 7 == 0:
        print("*", end='、')
