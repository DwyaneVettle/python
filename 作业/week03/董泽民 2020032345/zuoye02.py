# 2022/3/9 11:44
jiage = int(input("请输入价格："))
if 100 <= jiage <= 1000:
    print(f"价格为{jiage},打折后为：{jiage * 0.95}")
elif 1001 <= jiage <= 3000:
    print(f"价格为{jiage},打折后为：{jiage * 0.9}")
elif 3001 <= jiage <= 5000:
    print(f"价格为{jiage},打折后为：{jiage * 0.8}")
elif jiage >= 5000:
    print(f"价格为{jiage},打折后为：{jiage * 0.6}")
else:
    print(f"价格为{jiage},不打折")
