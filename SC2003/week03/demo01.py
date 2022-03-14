# author by Michealzou@126.com
# 2022/3/7 14:05
# 字符串的格式化操作
# 1.%占位符可以预留变量的位置
name = '程茂恒'
age = 20
# print('我叫' + name + '今年' + str(age) + '岁。')
# 通过%占位符需要匹配变量的类型，%s表示传入字符串，%d表示传入十进制
# print('我叫%s,今天%d岁' % (name, age))
# 2.format()方法-变量与{}相对应，也可以使用索引的方式进行指向
# print('我叫{1},今年{0}岁'.format(age, name))
# 3.f-strings-在字符串前传入f引导，配合{参数}
print(f'我叫{name},今年{age}')

