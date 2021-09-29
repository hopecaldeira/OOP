class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.01, balance=0)
        self.checking = BankAccount(int_rate=0.01, balance=0)

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def display_user_balance(self):
        print(self.account.balance)
        return self
    
    def transfer_money(self, amount, user, ch1):
        self.account.balance -= amount
        user.account.balance += amount
        return self

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
