class Bankaccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return self.balance
        else:
            print("Insufficient balance")
    def display_balance(self):
        return self.balance

b1 = Bankaccount("Vani", 560)
print(b1.deposit(100))
print(b1.withdraw(50))
print(b1.display_balance())