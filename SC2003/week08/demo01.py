# author by Michealzou@126.com
# 2022/4/11 14:14
# 刮刮乐彩票的模拟
# 思路：通过列表的下标找到对应的元素
list01 = ["谢谢惠顾", "一等奖", "谢谢惠顾", "二等奖", "谢谢惠顾"]
# print(list01[1])
num = int(input("请抽奖(请抽取1-5之间的号码)："))
# 判断是否中奖
if 1 < num < 5:
    info = list01[num-1]
    print(info)
else:
    print("你的抽奖号码不在奖号之间，请重新输入")
