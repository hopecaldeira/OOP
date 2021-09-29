class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self
    
    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        return self

hope = User("Hope", "hope2@codingdojo.com")
jon = User("Jon", "jon1@codingdojo.com")
dave = User("Dave", "dave3@codingdojo.com")

hope.make_deposit(300).make_deposit(300).make_deposit(300).make_withdrawal(200).display_user_balance()
jon.make_deposit(20000).make_deposit(100000000).make_withdrawal(1000).make_withdrawal(500).display_user_balance()
dave.make_deposit(100).make_withdrawal(2).make_withdrawal(5).make_withdrawal(10).display_user_balance()
hope.transfer_money(200, dave).display_user_balance()