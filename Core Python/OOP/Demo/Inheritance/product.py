class Product:
    def __init__(self,id1,name1,price1):
        self.id=id1
        self.name=name1
        self.price=price1

    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid

    def getName(self): 
        return self.name
    def setName(self,newname):
        self.name=newname

    def getPrice(self):
        return self.price
    def setPrice(self,newprice):
        self.price=newprice

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tPrice={self.price}")

class Mobail(Product):
    def __init__(self, id1, name1, price1,sim_count):
        super().__init__(id1, name1, price1)
        self.sim_count=sim_count
    def getSim_count(self):
        return self.sim_count
    def setSim_count(self,nsim_count):
        self.sim_count=nsim_count
    def display(self):
        print(f'Sim_count={self.sim_count}\t')
        super().display()

class Laptop(Product):
    def __init__(self, id1, name1, price1,ram):
        super().__init__(id1, name1, price1)
        self.ram=ram
    def getRam(self):
        return self.ram
    def setRam(self,nram):
        self.ram=nram
    def display(self):
        print(f'Ram={self.ram}\t')
        super().display()

p1=Product(10,"Sunscreem",100)
m1=Mobail(14,"Vivo",120,2)
l1=Laptop(17,"Oppo",50000,8)
p1.display()
m1.display()
l1.display()