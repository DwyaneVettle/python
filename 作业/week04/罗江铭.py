sum = 0

i = 0

while i <= 100:
    sum += i

    i += 2

print(sum)

sum = 0

# range函数end时不包括当前数值，所有注意101.

for i in range(0, 101, 2):
    sum += i

print(sum)


for i in range (1,10):
    for j in range (1,10):
        print(i,"X",j,"=",i*j,"\t",end="")#end=""表示不换行
        if i == j:
            print("")
            break
