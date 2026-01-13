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


x = BankAccountClass('Adam', 101.11)
x.deposit(100)
x.withdraw(50)
x.display_balance()


