# author by Michealzou@126.com
# 2022/4/18 16:23
"""
练习：
经理：刘备，曹操，孙权
销售：刘备，张飞，关羽
财务：孙权，鲁肃，陆逊，周瑜
人事：曹操，关羽，典韦，大乔
请输出：既是经理还是销售的是谁
是人事不是经理的是谁
人事和销售都有职位的是谁
大乔是不是财务
"""
jingli = {"刘备", "曹操", "孙权"}
xiaoshou = {"刘备", "张飞", "关羽"}
caiwu = {"孙权", "鲁肃", "陆逊", "周瑜"}
renshi = {"曹操", "关羽", "典韦", "大乔"}
print(jingli & xiaoshou)
print(renshi - jingli)
print(renshi & xiaoshou)
print("大乔" in caiwu)
set01 = {"大乔"}
print(set01 < caiwu)


