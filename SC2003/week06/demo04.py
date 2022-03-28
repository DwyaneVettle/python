# author by Michealzou@126.com
# 2022/3/28 15:53
# 列表的遍历
list01 = ['python', 'java', 'php', 'html', 'js']
# 1.判断元素是否存在在列表中 in, not in
print('c++' in list01)
print('python' not in list01)
# 2.遍历所有元素-for,Collections
for items in list01:
    print(f'{items}太好学了')