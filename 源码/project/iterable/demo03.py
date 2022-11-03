# author by Michealzou@126.com
# 2022/11/1 21:25
# 创建多个图形管理器，进行迭代
# 图形类
class Graphic:
    pass


# 图形管理器类
class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):
        return GraphicIterator(self.__graphics)


# 图形迭代器类
class GraphicIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target) -1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp

manager = GraphicManager()
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
