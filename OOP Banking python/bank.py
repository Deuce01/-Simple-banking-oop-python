class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []  # List to hold all accounts

    def create_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} created for {account.account_holder}")

    def show_all_accounts(self):
        for account in self.accounts:
            print(f"Account Holder: {account.account_holder}, Account Number: {account.account_number}, Balance: {account.get_balance()}")

    def calculate_all_interests(self):
        for account in self.accounts:
            account.calculate_interest()
