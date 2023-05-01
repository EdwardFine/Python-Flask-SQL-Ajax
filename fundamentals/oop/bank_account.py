class BankAccount:
    # don't forget to add some default values for these parameters!
    
    all_accounts =[]
    
    def __init__(self, int_rate=0.01, balance=0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.intrest_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        # your code here
        if self.balance - amount >0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        # your code here
        if self.balance>0:
            self.balance += (self.balance*self.intrest_rate)
        else:
            print("No intrest payment")
        return self
    
    @classmethod
    def display_all_accounts(cls):
            for account in cls.all_accounts:
                account.display_account_info()


account1 = BankAccount()
account2 = BankAccount()

account1.deposit(50).deposit(100).deposit(25).withdraw(75).yield_interest().display_account_info()

account2.deposit(1000).deposit(500).withdraw(250).withdraw(100).withdraw(500).withdraw(1000).yield_interest().display_account_info()

BankAccount.display_all_accounts()