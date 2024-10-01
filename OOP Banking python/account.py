from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_holder, account_number, initial_balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self._balance = initial_balance  # Encapsulation (private attribute)
    
    @abstractmethod
    def calculate_interest(self):
        pass

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self._balance
