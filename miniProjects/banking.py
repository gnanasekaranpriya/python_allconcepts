# Create a BankAccount class with attributes owner and balance.
# Methods: deposit(), withdraw(), display_balance().
# Let user interact with the account through a while loop menu.
# Optional Challenge:
# Add multiple accounts using a dictionary of BankAccount objects
# Implement PIN verification

class bankaccount(): 
    def __init__(self, owner, balance): 
        self.owner  = owner 
        self.balance = balance 
    
    def deposit(self, amount):
        self.balance += amount 

    def withdraw(self, amount): 
        if self.balance < amount : 
            print('You currently do not have sufficient funds to withdraw money')
        else: 
            self.balance -= amount 
    
    def display_balance(self): 
        print(f'Current balance for {self.owner} is {self.balance}')

user1 = bankaccount('user1', 5000)
user1.display_balance()
user1.withdraw(200)
user1.display_balance()