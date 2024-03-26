"""
    pass语句表示什么都不做
    作用：当不清楚下一步要做什么的时候，占位，避免报错\
    常常配合条件判断，循环语句使用
"""
# answer = input("你是会员吗y/n：")
# if answer == 'y':
#     pass
# else:
#     pass

"""
    range()表示取值范围
        start:开始
        end：结束 -- 不包含
        step:步长
    - **range(stop)**：创建一个以(0,stop)之间的整数序列，步长为1；
    - **range(start,stop)**：创建一个(start,stop)之间的整数序列，步长为1；
    - **range(start,stop,step)**：创建一个(start,stop)之间的序列，步长为step。
"""
print(range(1, 100, 1))
for i in range(1, 100, 1):
    print("i在这里面")

