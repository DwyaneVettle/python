# author by Michealzou@126.com
# 2022/3/28 21:56
def fun01():
    while True:
        res = int(input('输入:'))
        if 0 < res < 9:
            break
        else:
            print('请选择正确刮奖：')
    return res - 1


list01 = ["谢谢惠顾", "一等奖", "三等奖", "谢谢惠顾", "谢谢惠顾", "三等奖", "二等奖", "谢谢惠顾"]
res = int(input("输入中奖号码："))
if 0 < res < len(list01):
    info = list01[res - 1]
    print(f"{info}")
else:
    print('请选择正确刮奖区')
