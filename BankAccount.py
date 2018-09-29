import types
class BankAccount(object):
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __repr__(self):
        return 'This account belongs to %s and contains %2d \n' % (self._name, self._balance)

    def get_name(self):
        return self._name

    def get_balance(self):
        return self._balance

    def show_balance(self):
        print('%s\'s balance is now %2d ' % (self._name, self._balance))

    def deposit(self, amount):
        if float(amount) < 0:
            print('You cannot deposit a negative amount')
        else:
            self._balance += float(amount)
            self.show_balance()

    def withdraw(self, amount):
        if float(amount) < 0:
            print('You cannot withdraw a negative amount')
        else:
            self._balance -= float(amount)
            self.show_balance()

    def transfer(self, recipient, amount):
        self._balance -= float(amount)
        recipient._balance += float(amount)
