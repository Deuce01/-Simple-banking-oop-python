from account import Account
class SavingsAccount(Account):
    def __init__(self, account_holder, account_number, initial_balance, interest_rate):
        super().__init__(account_holder, account_number, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance * self.interest_rate
        print(f"Interest on savings account {self.account_number}: {interest}")
        return interest
