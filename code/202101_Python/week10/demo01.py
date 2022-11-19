# author by Michealzou@126.com
# 2022/11/9 8:42
"""
    列表：[] 任意类型 可变可重复
    元组：() 单一的任意数据类型，按需分配,可重复
    字典：{} k-v结构，k不可重复，value可重复,可变
    集合：{} 单一的数据类型，不重复
    无序
"""
# 定义集合不能采用{}
set01 = set(["python", "java"])
# 如果集合有重复的元素，后面的元素会覆盖前面的
set02 = {"python", "java", "sql", "javascript", "php", "python"}

# 增加 add()
set02.add(123)
print(set02)

# 删除remove() discard() pop()
set02.remove("sql")

set02.discard("php")

set02.pop()  # 删除任意一个
print(set02)
# 遍历
set02 = {"python", "java", "sql", "javascript", "php", "python"}
for i in set02:
    print(i)
