


class Bank:
    def __init__(self):
        self.accounts = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_enabled = True

    def create_account(self, name, initial_balance):
        if name in self.accounts:
            print("Account already exists in Bank portal!")
            return None
        if initial_balance < 0:
            print("Initial balance must be positive value!")
            return None
        self.accounts[name] = initial_balance
        self.total_balance += initial_balance
        return name

    def get_account_balance(self, name):
        if name in self.accounts:
            return self.accounts[name]
        else:
            print("Account details not found!")
            return None

    def deposit(self, name, amount):
        if name in self.accounts:
            if amount > 0:
                self.accounts[name] += amount
                self.total_balance += amount
                print(f"Deposited successfully {amount} into account {name}'s.")
            else:
                print("Deposit amount must be positive value!")
        else:
            print("Account number not found!")

    def withdraw(self, name, amount):
        if name in self.accounts:
            if amount > 0:
                if self.accounts[name] >= amount:
                    self.accounts[name] -= amount
                    self.total_balance -= amount
                    print(f"Successfully withdrew {amount} from account {name}'s account.")
                    if self.total_balance < 0:
                        print("Bank is bankrupt!")
                else:
                    print("Insufficient balance in your account!")
            else:
                print("Withdrawal amount must be positive!")
        else:
            print("Account number not found in Bank portal!")

    def transfer(self, sender_name, recipient_name, amount):
        if sender_name in self.accounts and recipient_name in self.accounts:
            if amount > 0:
                if self.accounts[sender_name] >= amount:
                    self.accounts[sender_name] -= amount
                    self.accounts[recipient_name] += amount
                    print(f"Transferred has been successecfully{amount} from account {sender_name} to {recipient_name}.")
                    if self.total_balance < 0:
                        print("Bank is bankrupt!")
                else:
                    print("Insufficient funds!")
            else:
                print("Transfer amount must be positive!")
        else:
            print("One or both accounts not found!")

    def get_transaction_history(self, name):
        if name in self.accounts:
            print(f"Transaction history for account {name}:")
           
        else:
            print("Account not found!")

    def toggle_loan_feature(self, enabled):
        self.loan_enabled = enabled

    def process_loan(self, name):
        if name in self.accounts:
            if self.loan_enabled:
                loan_amount = 2 * self.accounts[name]
                self.accounts[name] += loan_amount
                self.total_loan_amount += loan_amount
                print(f"Loan of {loan_amount} processed for account {name}.")
            else:
                print("Loan feature is currently disabled.")
        else:
            print("Account not found!")


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, initial_balance):
        return self.bank.create_account(name, initial_balance)

    def get_total_balance(self):
        return self.bank.total_balance

    def get_total_loan_amount(self):
        return self.bank.total_loan_amount

    def toggle_loan_feature(self, enabled):
        self.bank.toggle_loan_feature(enabled)


class User:
    def __init__(self, bank, name):
        self.bank = bank
        self.name = name

    def create_account(self, initial_balance):
        return self.bank.create_account(self.name, initial_balance)

    def deposit(self, amount):
        self.bank.deposit(self.name, amount)

    def withdraw(self, amount):
        self.bank.withdraw(self.name, amount)

    def transfer(self, recipient_name, amount):
        self.bank.transfer(self.name, recipient_name, amount)

    def get_balance(self):
        return self.bank.get_account_balance(self.name)

    def get_transaction_history(self):
        self.bank.get_transaction_history(self.name)


# Create a bank instance
bank = Bank()

# Create Bank admin
admin = Admin(bank)

# Create users
farbiz = User(bank, "Farbiz")
afzzal = User(bank, "Afzzal")
tofazzal = User(bank, "Tofazzal")

# Create accounts for users
farbiz.create_account(1000)
afzzal.create_account(500)
tofazzal.create_account(50000)

# Perform Bank users operations
farbiz.deposit(500)
tofazzal.deposit(5005)
farbiz.withdraw(200)
farbiz.transfer("Afzzal", 300)

farbiz.get_balance()
tofazzal.get_balance()
farbiz.get_transaction_history()

admin.toggle_loan_feature(True)
bank.process_loan("Farbiz")

farbiz.get_balance()
tofazzal.get_balance()

# Bank Admin operations
print("Total available balance in bank:", admin.get_total_balance())
print("Total loan amount processed:", admin.get_total_loan_amount())


