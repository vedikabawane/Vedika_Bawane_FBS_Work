from abc import ABC,abstractmethod 
class Employee(ABC):
    def __init__(self, id1, name1, sal1):
        self.id = id1
        self.name = name1
        self.sal = sal1

    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getSal(self):
        return self.sal
    def setSal(self, newsal):
        self.sal = newsal

    @abstractmethod
    def calSal(self):
       pass

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tSal={self.sal}")


class Hr(Employee):
    def __init__(self, id1, name1, sal1, com):
        super().__init__(id1, name1, sal1)
        self.com = com

    def getCom(self):
        return self.com
    def setCom(self, ncom):
        self.com = ncom

    def calSal(self):
        print(f'Final Sal of Hr {self.sal + self.com}')


class Developer(Employee):
    def __init__(self, id1, name1, sal1, bonus):
        super().__init__(id1, name1, sal1)
        self.bonus = bonus

    def getBonus(self):
        return self.bonus
    def setBonus(self, nbonus):
        self.bonus = nbonus

    def calSal(self):
        print(f'Final Sal of Developer {self.sal + self.bonus}')


# e1 = Employee(10, "Vedika", 1234)
h1 = Hr(6, "Amisha", 3459, 785)
d1 = Developer(34, "Ashwini", 7895, 3455)

# e1.calSal()
# h1.calSal()
# d1.calSal()

li=[]
li.append(h1)
li.append(d1)
print(li)
for i in li:
    i.display()