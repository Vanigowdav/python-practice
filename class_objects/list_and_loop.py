class Name:
    def __init__(self, name):
        self.name = name
    def show(self, accounts):
        for name in accounts:
            print(name.name)
accounts = []
s1 = Name("Vani")
s2 = Name("Druv")
s3 = Name("Parav")
accounts.append(s1)
accounts.append(s2)
accounts.append(s3)
s1.show(accounts)
