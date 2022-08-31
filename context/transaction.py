class Transaction(object):

    def __init__(self, sender, reciver, currency):
        self._sender = sender
        self._reciver = reciver
        self._currency = currency

    def transfer(self, amount):
        if self.__validate_transaction(amount):
            self._sender.send_money(amount, self._reciver)
            self.__log_transaction(amount)

    def __validate_transaction(self, amount):
        return self._sender.is_active() and self._reciver.is_active() and \
               self._sender.validate_currency(self._currency) and \
               self._reciver.validate_currency(self._currency) and \
               self._sender.check_balance(amount)

    def __log_transaction(self, amount):
        pass