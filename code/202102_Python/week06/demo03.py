# author by Michealzou@126.com
# 2022/10/11 9:36
"""
    要求输出1-50之间5的倍数
    continue表示结束当前判断循环，继续执行下面的代码
"""
# 1.生成1-50的序列
for item in range(1, 51, 1):
    # print(item)
    # 2.判断item是不是5的倍数
    # if item % 5 == 0:
    #     print(item)
    if item % 5 != 0:
        continue
    print(item)
