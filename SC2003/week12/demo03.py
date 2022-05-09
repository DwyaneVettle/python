# author by Michealzou@126.com
# 2022/5/9 14:56
# 用递归函数实现斐波那契数
def fabonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fabonacci((num-1)) + fabonacci((num - 2))

num = int(input("请输入序列："))
for i in range(1,num-1):
    print(fabonacci(i))