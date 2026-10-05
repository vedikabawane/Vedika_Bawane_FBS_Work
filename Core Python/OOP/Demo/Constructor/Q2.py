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


p1 = Vehicle(101, "Toyota", 500000)
p2 = Vehicle(102, "Honda", 800000)

print(p1.getBrand())

p1.display()
p2.display()

p2.setPrice(700000)

p2.display()