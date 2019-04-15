class BankAccount:
    def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
        # your code here! (remember, this is where we specify the attributes for our class)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = 0
    def deposit(self, amount):
        # your code here
        self.balance+=amount
        return self
    def withdraw(self, amount):
        # your code here
        self.balance-=amount
        return self
    def display_account_info(self):
        # your code here
        print("The balance is:", self.balance)
    def yield_interest(self):
        # your code here
        self.balance += self.balance * self.int_rate
        return self

A = BankAccount(0.25,0)
B = BankAccount(0.5, 0)
A.deposit(10).deposit(10).withdraw(10).yield_interest().display_account_info()