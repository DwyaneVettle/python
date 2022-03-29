# author by Michealzou@126.com
# 2022/3/20 19:19
sum = 0
i = 0
while i <= 100:
    i += 1
    if i%2==0:
        sum +=i
print(sum)

s=0
for i in range(2,101,2):
    s+=i
print(s)

for i in range(1,10):
    for j in range(1,i+1):
        d = i * j
        print('%d*%d=%-2d'%(i,j,d),end = ' ' )
    print()