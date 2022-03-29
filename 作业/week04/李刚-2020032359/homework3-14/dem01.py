# 2022/3/14 17:42
# 用for循环和while循环求100以内偶数的和
j = 0
for i in range(101):
    if i % 2 == 0:
        j += i
print(j)

print("---------------------------")

i = 1
h = 0
while i <= 100:
    if i % 2 == 0:
        h += i
    i += 1
print(h)
