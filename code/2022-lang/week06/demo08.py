"""
    字典生成式：
        {k:v for k,v in zip(key,value)}
"""
keys = ["name", "gender", "age"]
values = ["micheal", "男", 18]
dict01 = {key: value for key, value in zip(keys, values)}
print(dict01)
