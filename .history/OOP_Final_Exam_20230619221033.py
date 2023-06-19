# class Bank:
#     def __init__(self):
#         self.accounts = {}
#         self.total_balance = 0
#         self.total_loan_amount = 0
#         self.loan_enabled = True

#     def create_account(self, name, initial_balance):
#         if name in self.accounts:
#             print("Account already exists!")
#             return None
#         if initial_balance < 0:
#             print("Initial balance cannot be negative!")
#             return None
#         self.accounts[name] = initial_balance
#         self.total_balance += initial_balance
#         return name

#     def get_account_balance(self, name):
#         if name in self.accounts:
#             return self.accounts[name]
#         else:
#             print("Account not found!")
#             return None

#     def deposit(self, name, amount):
#         if name in self.accounts:
#             if amount > 0:
#                 self.accounts[name] += amount
#                 self.total_balance += amount
#                 print(f"Deposited {amount} into account {name}.")
#             else:
#                 print("Deposit amount must be positive!")
#         else:
#             print("Account not found!")

#     def withdraw(self, name, amount):
#         if name in self.accounts:
#             if amount > 0:
#                 if self.accounts[name] >= amount:
#                     self.accounts[name] -= amount
#                     self.total_balance -= amount
#                     print(f"Withdrew {amount} from account {name}.")
#                 else:
#                     print("Insufficient funds!")
#             else:
#                 print("Withdrawal amount must be positive!")
#         else:
#             print("Account not found!")

#     def transfer(self, sender_name, recipient_name, amount):
#         if sender_name in self.accounts and recipient_name in self.accounts:
#             if amount > 0:
#                 if self.accounts[sender_name] >= amount:
#                     self.accounts[sender_name] -= amount
#                     self.accounts[recipient_name] += amount
#                     print(f"Transferred {amount} from account {sender_name} to {recipient_name}.")
#                 else:
#                     print("Insufficient funds!")
#             else:
#                 print("Transfer amount must be positive!")
#         else:
#             print("One or both accounts not found!")

#     def get_transaction_history(self, name):
#         if name in self.accounts:
#             print(f"Transaction history for account {name}:")
          
#         else:
#             print("Account not found!")

#     def toggle_loan_feature(self, enabled):
#         self.loan_enabled = enabled

#     def process_loan(self, name):
#         if name in self.accounts:
#             if self.loan_enabled:
#                 loan_amount = 2 * self.accounts[name]
#                 self.accounts[name] += loan_amount
#                 self.total_loan_amount += loan_amount
#                 print(f"Loan of {loan_amount} processed for account {name}.")
#             else:
#                 print("Loan feature is currently disabled.")
#         else:
#             print("Account not found!")


# class User:
#     def __init__(self, bank, name):
#         self.bank = bank
#         self.name = name

#     def create_account(self, initial_balance):
#         return self.bank.create_account(self.name, initial_balance)

#     def deposit(self, amount):
#         self.bank.deposit(self.name, amount)

#     def withdraw(self, amount):
#         self.bank.withdraw(self.name, amount)

#     def transfer(self, recipient_name, amount):
#         self.bank.transfer(self.name, recipient_name, amount)

#     def get_balance(self):
#         return self.bank.get_account_balance(self.name)

#     def get_transaction_history(self):
#         self.bank.get_transaction_history(self)


