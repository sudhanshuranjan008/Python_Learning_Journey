# ------------------------------------------------------
# File: banking_system.py
# Date: 2024-12-31
# Author: Sudhanshu Ranjan
# ------------------------------------------------------

# Implement a banking system by creating a BankAccount class with methods to deposit, withdraw, and check balance

class BankAccount:
    def __init__(self, initial_balance: int = 0):
        """
        Constructor to initialize the bank account with an initial balance.
        The default balance is set to 0 if no initial balance is provided.
        """
        self.__available_amount = initial_balance  # Store the account balance as a private attribute

    def deposit(self, credit: int):
        """
        Method to deposit a certain amount into the account.
        It checks that the credit amount is positive before updating the balance.
        """
        if credit <= 0:  # Check if the credit amount is greater than 0
            print("Deposit amount must be greater than 0.")
            return  # Exit the method if the amount is invalid
        self.__available_amount += credit  # Add the deposit amount to the account balance
        print(f"Account credited with amount ₹ {credit}")

    def withdraw(self, debit: int):
        """
        Method to withdraw a certain amount from the account.
        It ensures the withdrawal amount is positive and there are sufficient funds.
        """
        if debit <= 0:  # Check if the debit amount is greater than 0
            print("Withdrawal amount must be greater than 0.")
            return  # Exit the method if the amount is invalid
        if debit > self.__available_amount:  # Check if there are enough funds in the account
            print("Insufficient funds for this withdrawal.")
            return  # Exit the method if the funds are insufficient
        self.__available_amount -= debit  # Deduct the withdrawal amount from the account balance
        print(f"Account debited with amount ₹ {debit}")

    def check_balance(self):
        """
        Method to check and display the current available balance in the account.
        """
        print(f"The available amount in the account is ₹ {self.__available_amount}")

# Main interaction with the user
acc123 = BankAccount(1000)  # Initialize the account with an initial balance of ₹1000

try:
    print("Hello! account 'acc123' holder. WELCOME!")  # Display a welcome message
    # Prompt the user to select a transaction type (deposit, withdraw, or check balance)
    selection = int(input("Please enter the number for respective transaction from below:\n 1- Deposit \n 2- Withdraw \n 3- Check Balance \n Please enter the choice here: "))

    if selection == 1:  # If user selects deposit
        credit = int(input("Please enter the amount to be deposited: ₹ "))  # Prompt for deposit amount
        acc123.deposit(credit)  # Call the deposit method

    elif selection == 2:  # If user selects withdraw
        debit = int(input("Please enter the amount to be withdrawn: ₹ "))  # Prompt for withdrawal amount
        acc123.withdraw(debit)  # Call the withdraw method

    elif selection == 3:  # If user selects check balance
        acc123.check_balance()  # Call the check_balance method

    else:  # If user enters an invalid choice
        print("Invalid choice, please enter a valid input.")

except ValueError:  # Catch any invalid input that cannot be converted to an integer
    print("Invalid input. Please enter a valid number for the transaction.")


