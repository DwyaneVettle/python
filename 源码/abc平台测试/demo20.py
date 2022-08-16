# author by Michealzou@126.com
# 2022/8/5 13:07
# 8.2
# 统计["苹果","香蕉","苹果","梨","苹果","橘子"] 出现最多次数的水果及出现的次数
fruits = ["苹果", "香蕉", "苹果", "苹果", "苹果", "橘子"]
max = 0
fruit_name = ""
for fruit in fruits:
    fruit_count = fruits.count(fruit)


    if fruit_count > max:
        max = fruit_count
        fruit_name = fruit

print("出现最多的水果为:{},共出现了{}次".format(fruit_name, max))
