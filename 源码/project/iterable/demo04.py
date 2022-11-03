# author by Michealzou@126.com
# 2022/11/1 21:41
# 员工管理器记录多个员工，迭代员工管理器
class Employee:
    pass


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def __iter__(self):
        return EmployeeItrater(self.employees)

class EmployeeItrater:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


# 创建对象
employee = EmployeeManager()
employee.add_employee(Employee())
# 遍历
# for emp in employee:
#     print(emp)
iterator = employee.__iter__()
while True:
    try:
        items = iterator.__next__()
        print(items)
    except StopIteration:
        break