# 2.做一个超市购物判断：100-1000-95折，1001-3000-9折，3001-5000-8折 5000-6折
# 将input（）方法接收的字符转换为int类型
score = int(input("请输入购物金额:"))
if 1000 >= score >= 100:
    print("打95折")
elif 3000 >= score >= 1001:
    print("打9折")
elif 5000 >= score >= 3001:
    print("打8折")
elif score > 5000:
    print("打6折")
else:
    print("不满足条件")