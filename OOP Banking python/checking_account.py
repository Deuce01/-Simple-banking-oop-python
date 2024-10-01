from account import Account
class CheckingAccount(Account):
    def __init__(self, account_holder, account_number, initial_balance):
        super().__init__(account_holder, account_number, initial_balance)

    def calculate_interest(self):
        print(f"Checking accounts do not accrue interest.")
        return 0
