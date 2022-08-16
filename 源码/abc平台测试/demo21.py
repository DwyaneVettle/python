# author by Michealzou@126.com
# 2022/8/6 8:52
# 8.3
# 字符串以什么开头startswith，以什么结尾endswith  返回bool（真、假）
file = "test.doc"
heros = ["zwj", "gy", "zy", "lb"]

# ********** End *********

if file.endswith(".doc"):
    print("hello,there is test.doc")

# ********** End *********

for hero in heros:
    if hero.startswith("z"):
        print(hero)
