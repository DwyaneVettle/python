import numpy as np

# 自定义复合类型
# 数据-每个元组为一个对象-> 姓名、成绩、年龄
data = [
    ('zs', [90, 78, 88], 20),
    ('ls', [92, 89, 78], 21),
    ('ww', [90, 85, 83], 21)]
# a = np.array(data)
# print(a)  # ValueError，需指定数据类型
# 1.第一种设置dtype的方式
# U2表示2个unicode字符，3int32表示出现32位二进制出现3个
a = np.array(data, dtype='U2, 3int32, int32')
print(a)
print(a[1][1])  # 获取李四的成绩 [92 89 78]
print("1=====================================")

# 2.第二种设置dtype的方式-列表+元组,取别名
a = np.array(data, dtype=[('name', 'str', 2),
                          ('scores', 'int32', 3),
                          ('age', 'int32', 1)])
print(a)
print(a[2]['age'])  # 获取ww的年龄 21
print("2=====================================")

# 3.第三种设置dtype的方式-字典+列表，标注字段名和类型
a = np.array(data, dtype={
    'names': ['name', 'scores', 'age'],
    'formats': ['U2', '3int32', 'int32']
})
print(a)
print(a[1]['name'])  # 获取第二个人名字
print("3=====================================")

# 4.第四种设置dtype的方式-别名+类型+字节拼音量
d = np.array(data, dtype={'names': ('U3', 0),
                          'scores': ('3int32', 16),
                          'ages': ('int32', 28)})
# d.itemsize表示内存空间占多少字节
print(d[0]['names'], d[0]['scores'], d.itemsize)
print("4=====================================")


# 5.第五种设置dtype的方式（了解）
e = np.array([0x1234, 0x5667],
             dtype=('u2', {'lowc': ('u1', 0),
                            'hignc': ('u1', 1)}))
print('%x' % e[0])
print('%x %x' % (e['lowc'][0], e['hignc'][0]))
print("5=====================================")


# 6.测试日期类型数组-数组中存储日期
dates = ['2023-01-01', '2023', '2023-02',
         '2024-01-01', '2024-01-01 10:10:10']
dates = np.array(dates)
# print(dates, dates.dtype)
# 输出结果：['2023-01-01' '2023' '2023-01' '2024-01-01' '2024-01-01 10:10:10'] <U19
# <U19中<表示字节序，U19表示Unicode出现了19个字符，即最大2024-01-01 10:10:10
# 以上输出都是字符串，不是日期格式，如果需要日期格式，需要如下转换
dates = dates.astype('M8[D]')
print(dates, dates.dtype)
print(dates[2] - dates[1])  # 31 days
