# bank_account.py

class BankAccount:
    """
    A simple BankAccount class that supports deposit, withdrawal, 
    and displaying the current balance.
    """

    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds exist.
        Returns True if successful, otherwise False.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        """Display the current account balance with two decimal places."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
