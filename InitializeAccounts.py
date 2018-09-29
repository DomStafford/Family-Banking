from BankAccount import BankAccount
from random import randint

path = 'bank_accounts.txt'

Dom = BankAccount('Dom', randint(-1000, 1000))
Lex = BankAccount('Lex', randint(-1000, 1000))
Dan = BankAccount('Dan', randint(-1000, 1000))
Henry = BankAccount('Henry', randint(-1000, 1000))
Bill = BankAccount('Bill', randint(-1000, 1000))

with open(path, 'w') as f:
    for person in [Dom, Lex, Dan, Henry, Bill]:
        f.write('%s: %d \n' % (person.get_name(), person.get_balance()))
    f.close()

