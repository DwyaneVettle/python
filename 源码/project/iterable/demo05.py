# author by Michealzou@126.com
# 2022/11/2 20:43
class MyRange:
    def __init__(self, stop_value):
        self.stop_value = stop_value

    def __iter__(self):
        return MyRangeIterator(self.stop_value)

class MyRangeIterator:
    def __init__(self, end_value):
        self.__end_value = end_value
        self.__index = 0

    def __next__(self):
        if self.__index == self.__end_value:
            raise StopIteration
        temp = self.__index
        self.__index += 1
        return temp

for item in MyRange(9999):
    print(item)