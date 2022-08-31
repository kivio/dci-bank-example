
class Currency(object):

    def __init__(self, currency):
        self.__currency = currency

    def __eq__(self, other):
       if isinstance(other, str):
        return self.__currency == other

       return False