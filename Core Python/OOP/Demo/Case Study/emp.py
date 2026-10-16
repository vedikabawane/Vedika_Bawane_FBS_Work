from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,id=0,name=None,sal=0):
        self.id=id
        self.name=name
        self.sal=sal
        
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
    
    @abstractmethod
    def calSal(self):
        pass
    
    def __str__(self):
        return f"Id= {self.id}\tName={self.name}\tSal={self.sal}" 
    
    def display(self):
        print(f"Id= {self.id}\tName={self.name}\tSal={self.sal}")