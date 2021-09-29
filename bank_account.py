class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = .01
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance *= (1 + self.int_rate)
        return self
    
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

a1 = BankAccount("a1", 600)
a2 = BankAccount("a2", 400)

a1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
a2.deposit(600).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()