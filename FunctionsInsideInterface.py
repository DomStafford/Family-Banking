from BankAccount import BankAccount

SERVICE_MAPPING = {'1': 'show_balance',
                   '2': 'deposit',
                   '3': 'withdraw',
                   '4': 'transfer'}


def interact(accounts):
    account_names = [account.get_name() for account in accounts]
    account = _account_selection(account_names, accounts)
    account_index = account_names.index(account)
    service = _service_selection(account)
    if service in ['1', '2', '3', '4']:
        method = accounts[account_index].__getattribute__(SERVICE_MAPPING[service])
        if service == '1':
            method()
        elif service in ['2', '3']:
            amount = raw_input('How much?')
            method(amount)
        else:
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


def _request_user_input(request_message, valid_responses, error_message):
    response = raw_input(request_message)
    if response not in valid_responses:
        print(error_message)
        response = None
        while response is None:
            response = raw_input(request_message)
            if response not in valid_responses:
                print(error_message)
                response = None
    return response


def _service_selection(account):
    return _request_user_input('Hi, ' + account + '. What would you like to do? \n 1. Check balance' 
                                                  '\n 2. Deposit \n 3. Withdraw \n 4. Transfer \n 5. Exit \n',
                               ['1', '2', '3', '4', '5'], 'Please choose a number from 1 to 5.')


def _account_selection(account_names, accounts):
    choice = raw_input('Welcome to the Family Banking App. Who is this?')
    if choice not in account_names:
        print('This person does not have an account. The people with accounts are: ' + ', '.join(account_names) + '.')
        new_account = _request_user_input('Do you wish to make an account for ' + choice + '? (Y/N)',
                                          ['Y', 'N'], 'Invalid response. Try again.')
        if new_account == 'Y':
            amount_to_deposit = raw_input('How much would you like to deposit in this (' + choice + '\'s) account?')
            accounts.append(BankAccount(choice, float(amount_to_deposit)))
            account_names.append(choice)
            return choice
        else:
            print('Try again, then. Who is this?')
            choice = _account_selection(account_names, accounts)
        return choice
    return choice


def _get_recipient(account_names):
    return _request_user_input('Who would you like to pay?', account_names,
                               'This person does not have an account here.')


def _additional_service():
    return _request_user_input('Service completed. Is another service required? (Y/N)',
                               ['Y', 'N'], 'Not a valid input. Try again.')
