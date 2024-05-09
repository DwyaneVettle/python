# 练习：接收用户输入的一个四位数，使用函数计算该四位数每个位置上的数字相加之和
def each_unit_sum(number):
    result = number % 10  # 个位
    result += number // 10 % 10
    result += number // 100 % 10
    result += number // 1000
    return result
sum = each_unit_sum(1234)
print(sum)
sum01 = each_unit_sum(5678)
print(sum01)
