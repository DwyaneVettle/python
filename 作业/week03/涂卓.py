# author by Michealzou@126.com
# 2022/3/13 20:21
#水仙花数：3位数每个位置上的数的立方之和为他本身
for n in range(100,1000):
    i = n//100#百位
    j = (n-1 * 100)//10#十位
    k = n % 10#个位
    if n == i**3 + j**3 + k**3:
        print('100到1000之间的水仙花数是',n)

#根据消费金额进行打折
score = float(input('请输入金额：'))
c = 0.1
if 1 < score < 100:
    c = score * 1
    print('应付金额为', c)
elif 100 <= score <= 1001:
    c = score*0.95
    print('应付金额为', c)
elif 1001 <= score <= 3000:
    c = score*0.9
    print('应付金额为', c)
elif 3001 <= score <= 5000:
    c = score*0.8
    print('应付金额为', c)
elif 5001 <= score:
    c = score*0.6
    print('应付金额为', c)
else:
    print('请输入正确的金额')