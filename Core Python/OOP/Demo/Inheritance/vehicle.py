class Vehicle:
    def __init__(self, number1, brand1, price1):
        self.number = number1
        self.brand = brand1
        self.price = price1

    def getNumber(self):
        return self.number
    def setNumber(self, newnumber):
        self.number = newnumber

    def getBrand(self):
        return self.brand
    def setBrand(self, newbrand):
        self.brand = newbrand

    def getPrice(self):
        return self.price
    def setPrice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Number={self.number}\tBrand={self.brand}\tPrice={self.price}")

class Car(Vehicle):
    def __init__(self, number1, brand1, price1,doors):
        super().__init__(number1, brand1, price1)
        self.doors=doors
    def getDoors(self):
        return self.doors
    def setDoors(self,ndoors):
        self.doors=ndoors
    def display(self):
        print(f'Doors={self.doors}\t')
        super().display()

class Bus(Vehicle):
    def __init__(self, number1, brand1, price1,sets):
        super().__init__(number1, brand1, price1)
        self.sets=sets
    def getSets(self):
        return self.sets
    def setSets(self,nsets):
        self.sets=nsets
    def display(self):
        print(f'Sets={self.sets}\t')
        super().display()


v1 = Vehicle(101, "Toyota", 500000)
c1 = Car(101, "BMW", 700000,4)
b1 = Bus(101, "TATA", 900000,50)
v1.display()
c1.display()
b1.display()