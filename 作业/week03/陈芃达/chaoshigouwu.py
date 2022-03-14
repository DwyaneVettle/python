# 2022/3/13 20:39
Jiage = int(input('请输入价格：'))
if 100 <= Jiage <= 1000:
    print(f'您本次的商品将打9.5折，折后的价格为：{Jiage * 0.95}')
elif 1001 <= Jiage <= 3000:
    print(f'您本次的商品将打9折，折后的价格为：{Jiage * 0.9}')
elif 3001 <= Jiage <= 5000:
    print(f'您本次的商品将打8折，折后的价格为：{Jiage * 0.8}')
elif Jiage > 5000:
    print(f'您本次的商品将打6折，折后的价格为：{Jiage * 0.6}')
else:
    print(f'您本次的商品价格为：{Jiage}')

