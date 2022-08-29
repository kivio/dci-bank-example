from re import L
from data.account import Account

class SenderAccount(Account):

    def checkBalance(self, amount):
        return self.balance >= amount

    def sendMoney(self, amount):
        self.balance -= amount