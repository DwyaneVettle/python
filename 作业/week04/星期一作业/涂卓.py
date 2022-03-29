# author by Michealzou@126.com
# 2022/3/20 11:50

i = 0
j = 0
while i <= 100:
    i += 1
    if i % 2 == 0:
        #i除以2余为0时j等于j+i
        j += i
print(j)


s=0
for x in range(0,101,2):#x从0开始到101每隔两个数取一个数
    s+=x
    #print(x)
print(s)


for a in range(1,10):
    for b in range(1,1+a):
        print(b,'*',a,'=',a*b,'  ',end='')
    print('')