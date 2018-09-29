from BankAccount import BankAccount
from FunctionsInsideInterface import interact

path = 'bank_accounts.txt'
accounts = []
with open(path, 'r') as f:
    for line in f:
        separated_line = line.split(':')
        accounts.append(BankAccount(separated_line[0], float(separated_line[1])))

interact(accounts)
print('Thank you for using the app. Updating all balances.')

with open(path, 'w') as f:
    for person in accounts:
        f.write('%s: %d \n' % (person.get_name(), float(person.get_balance())))
    f.close()
