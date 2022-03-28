# author by Michealzou@126.com
# 2022/3/28 17:04
# 列表的修改
list01 = ['python', 'java', 'php', 'html', 'js']
# 1.以直接赋值的方式
list01[3] = 'css'
print(list01)
# 2.以切片方式
list01[2:5] = ['函数', 'class', 'object']
print(list01)