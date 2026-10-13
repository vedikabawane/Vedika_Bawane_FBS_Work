from abc import ABC,abstractmethod
class Vehical(ABC):
    def __init__(self,cNo,color):
        self.cno=cNo
        self.color = color
    def getCno(self):
        return self.cno
    def setCno(self,neno):
        self.setCno=neno

    def getColor(self):
        return self.color
    def setCol(self,nCol):
        self.color=nCol
    
    @abstractmethod
    def brake(self):
        pass
    def __str__(self):
        return f'Che No={self.cno} Color={self.color}'

class Car(Vehical):
    def brake(self):
        print('This is the brake of car')

c=Car(12,'black')
print(c)
c.brake()