"""
    列表切片：
        list[start:stop:step]
        start：表示开始下标-包含
        stop：表示结束的下标-不包含
        step：表示切片的步长
"""
list01 = list(["java", "python", "c++", "javascript", "python"])
print(list01[1:4:2])
print(list01[::2])  # ['java', 'c++', 'python']
print(list01[:3:])
print("======")
# 1."c++", "javascript"
print(list01[-3:-1])
# 2.python  python
print(list01[-4::3])
# 3.java  javascript
print(list01[-5:-1:3])
