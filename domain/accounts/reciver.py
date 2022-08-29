from data.account import Account


class ReciverAccount(Account):

    def addMoney(self, amount):
        self.balance += amount