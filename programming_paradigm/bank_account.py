# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = initial_balance
    
    def deposit(self, amount):
        """Add a specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraw a specified amount if sufficient funds are available."""
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
