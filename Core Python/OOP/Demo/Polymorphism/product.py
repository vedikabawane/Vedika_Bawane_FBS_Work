
class Product:
    def __init__(self, id1, name1, price1):
        self.id = id1
        self.name = name1
        self.price = price1

    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getPrice(self):
        return self.price
    def setPrice(self, newprice):
        self.price = newprice

    def calPrice(self):
        print(f'Final Price of Product {self.price}')

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tPrice={self.price}")


class Mobile(Product):
    def __init__(self, id1, name1, price1, sim_count):
        super().__init__(id1, name1, price1)
        self.sim_count = sim_count

    def getSim_count(self):
        return self.sim_count
    def setSim_count(self, nsim_count):
        self.sim_count = nsim_count

    def calPrice(self):
        print(f'Final Price of Mobile {self.price + 500}')

    def display(self):
        print(f'Sim_count={self.sim_count}\t')
        super().display()


class Laptop(Product):
    def __init__(self, id1, name1, price1, ram):
        super().__init__(id1, name1, price1)
        self.ram = ram

    def getRam(self):
        return self.ram
    def setRam(self, nram):
        self.ram = nram

    def calPrice(self):
        print(f'Final Price of Laptop {self.price + 1000}')

    def display(self):
        print(f'Ram={self.ram}\t')
        super().display()


p1 = Product(10, "Sunscreen", 100)
m1 = Mobile(14, "Vivo", 12000, 2)
l1 = Laptop(17, "HP", 50000, 8)

p1.calPrice()
m1.calPrice()
l1.calPrice()
