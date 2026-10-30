class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(f"Your account has been withdrawn by rupees {amount}")
            return self.balance
        else:
            raise ValueError("Your account has insufficient balance")
b1 = BankAccount(500)
b2 = BankAccount(50)
print(b1.deposit(50))
print(b2.deposit(100))
b1.withdraw(60)
b2.withdraw(700)
