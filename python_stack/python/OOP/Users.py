class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.name, "has", self.account_balance, "in the account")
    def transfer_money(self, other_user, amount):
        self.withdraw(amount)
        other_user.deposit(amount)
        return self
    
john = User("John","john@john.com")
doe = User("Doe", "doe@doe.com")

john.deposit(100).deposit(100).withdraw(150).display_user_balance()
john.transfer_money(doe,25).display_user_balance()