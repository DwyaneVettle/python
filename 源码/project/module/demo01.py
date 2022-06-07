# author by Michealzou@126.com
# 2022/5/30 15:33
"""
验证码

"""
"""
随机生成6位的验证码（字母数字随机组合，包含大小写）
chr()函数返回值是当前整数对应的ascii字符。
"""
import random


def verifycode():
    code_list = ''
    # 每一位验证码都有三种可能（大写字母，小写字母，数字）
    for i in range(6):  # 控制验证码生成的位数
        state = random.randint(1, 3)
        if state == 1:
            # ASCII编码集中大写字母A-Z对应65-90位
            first_kind = random.randint(65, 90)  # 大写字母
            random_uppercase = chr(first_kind)
            code_list = code_list + random_uppercase

        elif state == 2:
            # ASCII编码集中小写字母a-z对应97-122位
            second_kinds = random.randint(97, 122)  # 小写字母
            random_lowercase = chr(second_kinds)
            code_list = code_list + random_lowercase
        elif state == 3:
            third_kinds = random.randint(0, 9)
            code_list = code_list + str(third_kinds)
    return code_list


if __name__ == '__main__':
    verifycode = verifycode()
    print(verifycode)
