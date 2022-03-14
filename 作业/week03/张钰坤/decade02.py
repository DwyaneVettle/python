decade = int(input('请输入价格：'))
if 100 <= decade <= 1000:
    print(f'您本次的商品将打9.5折，折后的价格为：{decade * 0.95}')
elif 1001 <= decade <= 3000:
    print(f'您本次的商品将打9折，折后的价格为：{decade * 0.9}')
elif 3001 <= decade <= 5000:
    print(f'您本次的商品将打8折，折后的价格为：{decade * 0.8}')
elif decade > 5000:
    print(f'您本次的商品将打6折，折后的价格为：{decade * 0.6}')
else:
    print(f'您本次的商品价格为：{decade}')