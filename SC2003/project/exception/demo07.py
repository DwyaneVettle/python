# author by Michealzou@126.com
# 2022/5/31 8:36
# 自定义CustomError异常类
class CustomError(Exception):
    pass


try:
    pass
    raise CustomError("出现客户端异常")
except CustomError as e:
    print(e)