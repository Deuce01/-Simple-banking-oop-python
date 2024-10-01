from savings_account import SavingsAccount
from checking_account import CheckingAccount
from bank import Bank 
# Create a bank
my_bank = Bank("My Local Bank")

# Create a SavingsAccount and CheckingAccount
savings_acc = SavingsAccount("Alice", "SA123", 1000, 0.05)
checking_acc = CheckingAccount("Bob", "CA456", 500)

# Add accounts to the bank
my_bank.create_account(savings_acc)
my_bank.create_account(checking_acc)

# Show all accounts
my_bank.show_all_accounts()

# Deposit money into accounts
savings_acc.deposit(500)
checking_acc.deposit(200)

# Withdraw money from accounts
savings_acc.withdraw(300)
checking_acc.withdraw(100)

# Calculate interest for all accounts
my_bank.calculate_all_interests()

# Show all accounts after transactions
my_bank.show_all_accounts()
