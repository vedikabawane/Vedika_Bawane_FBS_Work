from emp import Employee
class Hr(Employee):
    def __init__(self, id, name, sal,com):
        super().__init__(id, name, sal)
        self.com=com
    def getCom(self):
        return self.com
    def setCom(self,ncom):
        self.com=ncom
    
    def calSal(self):
        print(f"Final Sal of HR {self.sal+self.com}")
    
    def __str__(self):
        return super().__str__() +f"\t Com= {self.com}"
    
    def display(self):
        print(f"Com= {self.com}\t")
        super().display()
# Class Hr Ends Here........C..