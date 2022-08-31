from data.account import Account

class SenderAccount(object):

    def __init__(self, account):
        self._account = account

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            return getattr(self._account, name)

    def check_balance(self, amount):
        return self.balance >= amount

    def send_money(self, amount, reciver):
        self.balance -= amount
        reciver.add_money(amount)