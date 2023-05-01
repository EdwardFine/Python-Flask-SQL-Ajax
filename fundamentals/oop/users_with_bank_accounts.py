class BankAccount:
    # don't forget to add some default values for these parameters!

    all_accounts = []

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
        if self.balance - amount > 0:
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
        if self.balance > 0:
            self.balance += (self.balance*self.intrest_rate)
        else:
            print("No intrest payment")
        return self

    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts=[]
        self.accounts.append(BankAccount(int_rate=0.02, balance=0))

    # other methods

    def open_account(self):
        self.accounts.append(BankAccount(int_rate=0.02, balance=0))
        return self
    
    def close_account(self,index):
        try:
            if index ==0:
                print("Cannot remove First Account")
            else:
                self.accounts.pop(index)
        except IndexError:
            print("Account does not exist")
        return self

    def make_deposit(self, amount,account=0):
        # your code here
        try:
            self.accounts[account].deposit(amount)
        except IndexError:
            print("Account does not exist")
        return self
    
    def make_withdrawl(self,amount,account=0):
        try:
            self.accounts[account].withdraw(amount)
        except IndexError:
            print("Account does not exist")
        return self
    
    def display_user_balance(self,account=0):
        try:
            self.accounts[account].display_account_info()
        except IndexError:
            print("Account does not exist")
        return self
    
    def transer_money(self,amount,other_user,sender_account=0,other_account=0):
        try:
            self.make_withdrawl(amount,sender_account)
            if amount <= self.accounts[sender_account].balance:
                try:
                    other_user.accounts[other_account].deposit(amount)
                except IndexError:
                    print("Recipient's account does not exist")
                    self.make_deposit(amount)
        except IndexError:
            print("Sender's account does not exist")
        return self

user1 = User("Lightning Mcqueen","cachow@gmail.com")
user1.make_deposit(500)
user1.display_user_balance()

user2 = User("Tow Mater","tractortipper@yahoo.com")
user2.display_user_balance()

user1.transer_money(250,user2).display_user_balance()
user2.display_user_balance()
print("")
user1.transer_money(100,user2,0,1).display_user_balance()
user2.display_user_balance()
print("")
user1.transer_money(100,user2,1,0).display_user_balance()
user2.display_user_balance()
print("")
user1.transer_money(500,user2).display_user_balance()
user2.display_user_balance()
