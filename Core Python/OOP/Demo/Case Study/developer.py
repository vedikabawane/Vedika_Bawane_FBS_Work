from emp import Employee
class Devloper(Employee):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus=bonus
    def getBonus(self):
        return self.bonus
    def setBonus(self,ncom):
        self.bonus=ncom
    
    def calSal(self):
        print(f"Fianal Sal of Devloper {self.sal+self.bonus}")
    
    def __str__(self):
        return super().__str__() +f"\tBOnus= {self.bonus}"
    
    def display(self):
        print(f"Com= {self.bonus}\t")
        return super().display()