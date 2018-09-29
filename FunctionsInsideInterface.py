SERVICE_MAPPING = {'1': 'show_balance',
                   '2': 'deposit',
                   '3': 'withdraw',
                   '4': 'transfer'}


def interact(accounts):
    account_names = [account.get_name() for account in accounts]
    print('Welcome to the Family Banking App. Who is this?\n')
    account = _account_selection(account_names)
    account_index = account_names.index(account)

    print('What would you like to do? \n 1. Check balance \n 2. Deposit \n 3. Withdraw \n 4. Transfer \n 5. Exit')

    service = _service_selection()

    if service in ['1', '2', '3', '4']:
        method = accounts[account_index].__getattribute__(SERVICE_MAPPING[service])
        if service == '1':
            method()

        if service in ['2', '3']:
            amount = raw_input('How much?')
            method(amount)

        if service == '4':
            recipient = _get_recipient(account_names)
            recipient_index = account_names.index(recipient)
            amount = raw_input('How much would you like to pay ' + recipient + '?')
            method(accounts[recipient_index], amount)

        additional_service = _additional_service()
        if additional_service == 'Y':
            interact(accounts)
        else:
            return
    else:
        return


def _service_selection():
    choice = raw_input()
    if choice not in ['1', '2', '3', '4', '5']:
        print('Please choose a number from 1 to 5.')
        choice = _service_selection()
    return choice


def _account_selection(account_names):
    choice = raw_input()
    if choice not in account_names:
        print('This person does not have an account. The people with accounts are: ' + ', '.join(account_names) + '.')
        print('Try again. Who is this?')
        choice = _account_selection(account_names)
    return choice


def _get_recipient(account_names):
    recipient = None
    while recipient is None:
        recipient = raw_input('Who would you like to pay?')
        if recipient not in account_names:
            print('This person does not have an account here.')
            recipient = None
    return recipient


def _additional_service():
    additional_service = None
    while additional_service is None:
        additional_service = raw_input('Service completed. Is another service required? (Y/N)')
        if additional_service not in ['Y', 'N']:
            print('Not a valid input. Try again.')
            additional_service = None
    return additional_service
