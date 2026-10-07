class Employee:
    def __init__(self,id1,name1,sal1):
        self.id=id1
        self.name=name1
        self.sal=sal1

    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid

    def getName(self): 
        return self.name
    def setName(self,newname):
        self.name=newname

    def getSal(self):
        return self.sal
    def setSal(self,newid):
        self.sal=newid

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tSal={self.sal}")

#Emp Ends Here....

class Hr(Employee):
    def __init__(self, id1, name1, sal1,com):
        super().__init__(id1, name1, sal1)
        self.com=com
    def getCom(self):
        return self.com
    def setCom(self,ncom):
        self.com=ncom
    def display(self):
        print(f'Com={self.com}\t')
        super().display()
#Class Hr end here...

class Developer(Employee):
    def __init__(self, id1, name1, sal1,bonus):
        super().__init__(id1, name1, sal1)
        self.bonus=bonus
    def getBonus(self):
        return self.bonus
    def setCom(self,ncom):
        self.com=ncom
    def display(self):
        print(f'Bonus={self.bonus}\t')
        super().display()
#Class Developer end here...

e1=Employee(10,"Vedika",1234)
h1=Hr(6,'Amisha',3459,785)
d1=Developer(34,'Ashwini',7895,3455)
e1.display()
h1.display()
d1.display()
      