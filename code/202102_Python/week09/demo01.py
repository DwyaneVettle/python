# author by Michealzou@126.com
# 2022/11/1 8:39
# 字典
dict01 = {"四川": 5000, "重庆": 3000, "云南": 2000}
# dict02 = dict((1000, 2000)))
# 查询
print(dict01["四川"])
dict01.get("四川")
dict01.pop()
# 如果key不存在KeyError
if "贵州" in dict01:
    print(dict01["贵州"])

# 修改-通过Key
dict01["重庆"] = 3500

# 添加
dict01["贵州"] = 2000
print(dict01)

# 删除
del dict01["贵州"]

"""
    遍历
        1.遍历key-keys()
        2.遍历vlaue-values()
        3.遍历k.v-items()
"""
for key in dict01.keys():
    print(key)
    print(dict01[key])
print("----------------")
for value in dict01.values():
    print(value)
print("----------------")
for k, v in dict01.items():
    print(k, v)
