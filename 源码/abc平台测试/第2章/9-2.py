# author by Michealzou@126.com
# 2022/8/8 13:29
class Bank:
    def __init__(self, account, pwd):
        """
        银行创建账号的方法（初始化）
        """
        self.__account = account
        self.__balance = 0  # 银行账号的余额默认为0
        self.__pwd = pwd

    def save_money(self, money):
        """
        定义存钱的行为（方法）
        :param money: 需要存的钱
        """
        self.__balance += money
        print("您账户{}存入金额:{}".format(self.__account, money))

    def get_money(self, money):
        """
        取钱的方法
        :param money: 需要取出的钱
        """
        if money > self.__balance:
            print("Sorry，your credit is running low")
        else:
            self.__balance -= money
            print("your account {} take out:{}".format(self.__account, money))

    def query_money(self):
        """
        查看余额的方法
        :return:
        """
        print("your account {} balance is:{}".format(self.__account, self.__balance))

    def __update_pwd(self, pwd, update_pwd):  # 银行内部加密系统
        if pwd == self.__pwd:
            self.__pwd = update_pwd
            print("Congratulations,Your password was updated to:{}".format(update_pwd))
        else:
            print("Sorry,password error!")
# 创建update方法访问私有方法__update_pwd

# ******************** Begin *****************

    def update(self, pwd, update_pwd):  # 提供给用户操作的方法
        # 如何使用私有方法
        self.__update_pwd(pwd, update_pwd)


# 1.根据银行类创建a账户
# a执行取钱500，查询余额，将密码修改为666的操作

a = Bank('123', 123456)
a.get_money(500)
a.query_money()
a.update(123456, 666)
