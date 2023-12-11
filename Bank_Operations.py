import time
import sys


class Bank:
    bank_name = 'Indian Bank'
    bank_address = 'Chennai,India'

    def __init__(self,user_name,pan):
        self.user_name = user_name
        self.pan = pan
        self.balance = 0.0

        print('\nplease wait, while processing...')
        time.sleep(3)
        print(f'\nyour PAN NO  \'{pan}\' has successfully process ')
        print(f'\nwelcome, {user_name} from {Bank.bank_name} '
              f'{Bank.bank_address}')

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount
            print('please wait, while processing ...')
            time.sleep(3)
            print(f"\nyour amount {deposit_amount} has successfully "
                  f"deposited to"
                  f"your  account")
        else:
            print('\nERROR')

    def withdraw(self, withdraw_amount):
        if withdraw_amount < self.balance:
            self.balance -= withdraw_amount
            print('please wait, while processing ...')
            time.sleep(3)
            print(f'\n\nyour amount {withdraw_amount} has successfully '
                  f'debited')
            print(f'\n\nyour current balance is {self.balance} ')

    def view_balance(self):
        print('please wait, while processing ...')
        time.sleep(3)
        print(f'\n\nou have {self.balance} amount in your balance')




user_name = input('enter your Name : ')
pan = input('enter your PAN no : ')

bank = Bank(user_name,pan)

while True:
    user_input = int(input('\n1. view account balance'
                           '\n2. Add Money to the account'
                           '\n3. To get money'
                           '\n4. EXIT (if you would\'nt exit, loop will '
                           'starts '
                           'again)'
                           '\n ENTER : '))
    if user_input == 1:
        bank.view_balance()

    elif user_input == 2:
        deposit_amount = int(input('enter your amount to deposit to your '
                                   'account : '))
        bank.deposit(deposit_amount)

    elif user_input == 3:
        withdraw_amount = int(input('enter the amount wants to withdraw : '))
        bank.withdraw(withdraw_amount)

    elif user_input == 4 :
        sys.exit(f'THANK YOU {user_name}, vist again :)')

    else:
        print('\n INVALID INPUT')
        print('Try Again')
