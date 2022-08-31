from data.account import Account


class ReciverAccount(object):

    def __init__(self, account):
        self._account = account

    def add_money(self, amount):
        self.balance += amount

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            return getattr(self._account, name)