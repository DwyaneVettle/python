# author by Michealzou@126.com
# 2022/5/31 9:36
# 自定义上下文管理器
class File(object):
    """自定义实现上下文管理器"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


with File("a.txt", "wb") as f:
    f.write("哈哈哈,hahah".encode("utf8"))
    print("写入成功")
