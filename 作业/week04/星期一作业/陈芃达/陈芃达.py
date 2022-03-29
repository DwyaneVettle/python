# 2022/3/16 11:47
# 求100以内所有偶数的和
a = 0
for i in range(0, 101, 2):
    a += i
print(a)

print("-------------------------")

b = 0
c = 0
while c <= 100:
    b += c
    c += 2
    print(b)
