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


class SavingsAccount(BankAccount):
    def __init__(self, accountno1, name1, balance1, interest):
        super().__init__(accountno1, name1, balance1)
        self.interest = interest
    def getInterest(self):
        return self.interest
    def setInterest(self, ninterest):
        self.interest = ninterest
    def display(self):
        print(f"Interest={self.interest}%\t")
        super().display()


class CurrentAccount(BankAccount):
    def __init__(self, accountno1, name1, balance1, overdraft):
        super().__init__(accountno1, name1, balance1)
        self.overdraft = overdraft
    def getOverdraft(self):
        return self.overdraft
    def setOverdraft(self, noverdraft):
        self.overdraft = noverdraft
    def display(self):
        print(f"Overdraft={self.overdraft}\t")
        super().display()


b1 = BankAccount(101, "Vedika", 50000)
s1 = SavingsAccount(102, "Kartik", 70000, 6.5)
c1 = CurrentAccount(103, "Rahul", 90000, 50000)

b1.display()
s1.display()
c1.display()