# 2022/3/9 11:25
price = int(input('请输入价格：'))
if 100 <= price <= 1000:
    print(f'您本次的商品将打9.5折，折后的价格为：{price * 0.95}')
elif 1001 <= price <= 3000:
    print(f'您本次的商品将打9折，折后的价格为：{price * 0.9}')
elif 3001 <= price <= 5000:
    print(f'您本次的商品将打8折，折后的价格为：{price * 0.8}')
elif price > 5000:
    print(f'您本次的商品将打6折，折后的价格为：{price * 0.6}')
else:
    print(f'您本次的商品价格为：{price}')
