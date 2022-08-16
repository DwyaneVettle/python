# author by Michealzou@126.com
# 2022/8/4 16:31
# 4.1
# 根据给定的年份，判断是闰年还是平年？（四年一闰，百年不闰，四百年再闰）
year = 2004

# ********** Begin *********

# 能被4整除且不被100整除，或者可以被400整除
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(str(year)+'年是闰年')
else:
    print(str(year)+"是平年")

# ********** End *********