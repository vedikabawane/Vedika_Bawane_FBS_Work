class BankAccount:
    def __init__(self, accountno1, name1, balance1):
        self.accountno = accountno1
        self.name = name1
        self.balance = balance1

    def getAccountNo(self):
        return self.accountno
    def setAccountNo(self, newaccountno):
        self.accountno = newaccountno

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getBalance(self):
        return self.balance
    def setBalance(self, newbalance):
        self.balance = newbalance

    def display(self):
        print(f"Account No={self.accountno}\tName={self.name}\tBalance={self.balance}")


p1 = BankAccount(101, "Vedika", 50000)
p2 = BankAccount(102, "Priya", 60000)

print(p1.getName())

p1.display()
p2.display()

p2.setBalance(70000)

p2.display()