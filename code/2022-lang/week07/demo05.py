manager = {'曹操', '刘备', '孙权'}
tech = {'曹操', '刘备', '关羽', '张飞'}
print(manager & tech)
print(manager - tech)
print(tech - manager)
print('张飞' in manager)  # False
print(manager ^ tech)
print(len(manager | tech))


