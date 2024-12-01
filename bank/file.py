#1
class BankAccount:
    accounts = []

    def __init__(self, balance=0, interest_rate=0.05):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.accounts.append(self)
#2
    def deposit(self, amount):
        self.balance += amount
        return self
#3
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self
#4
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
#5
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self

#9    
    def display_all_accounts():
        for account in BankAccount.accounts:
            account.display_account_info()

#6
account1 = BankAccount(balance=1000, interest_rate=0.05)
account2 = BankAccount(balance=1500, interest_rate=0.02)

#7
account1.deposit(1000).deposit(1000).deposit(1000).withdraw(3000).yield_interest().display_account_info()

#8
account2.deposit(1500).deposit(1500).withdraw(100).withdraw(900).withdraw(1000).yield_interest().display_account_info()

#9
BankAccount.display_all_accounts()
