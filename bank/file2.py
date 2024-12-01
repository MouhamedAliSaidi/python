from file import BankAccount
#1
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(balance=0, interest_rate=0.02)
#2
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
#3
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
#4
    def display_user_balance(self):
        print(f"User: {self.name}, Email: {self.email}")
        self.account.display_account_info()
        return self


    #bonus adding user
user1 = User("Jane", "Jane@gmail.com")

    #testing relation with BankAccount class
user1.make_deposit(2000).make_withdrawal(500).display_user_balance()

