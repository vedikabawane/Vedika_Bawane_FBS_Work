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

p1=Product(10,"Sunscreem",100)
p2=Product(11,"Powder",80)
print(p1.getName())
p1.display()
p2.display()
p2.setPrice(60)
p2.display()