class BankAccount:
    def __init__(self, amount):
        self.account_balance = amount
    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
