class BankAccountClass:

    def __init__(self, user_name, balance):
        self.user_name = user_name
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited amount: {amount}')

    def withdraw(self, amount):
        if amount > self.balance:
            print ('Your balance is smaller than withdraw number')
        else:
            self.balance -= amount
            print(f'Withdraw amount: {amount}')

    def display_balance(self):
        print(f"{self.user_name}'s balance: {self.balance}")


abc = BankAccountClass('Adam', 101.11)
abc.deposit(100)
abc.withdraw(50)
abc.display_balance()


