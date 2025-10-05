class BankAccount:
    """A simple BankAccount class to demonstrate OOP concepts in Python."""

    def __init__(self, initial_balance=0.0):
        """
        Initialize the bank account with an optional starting balance.
        Default balance is 0.0 if not provided.
        """
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Deposit a given amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a given amount from the account.
        Returns True if successful, otherwise False if insufficient funds.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
