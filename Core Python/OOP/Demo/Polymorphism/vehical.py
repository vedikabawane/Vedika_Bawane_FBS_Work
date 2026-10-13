
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

    def calPrice(self):
        print(f'Final Price of Vehicle {self.price}')

    def display(self):
        print(f"Number={self.number}\tBrand={self.brand}\tPrice={self.price}")


class Car(Vehicle):
    def __init__(self, number1, brand1, price1, doors):
        super().__init__(number1, brand1, price1)
        self.doors = doors

    def getDoors(self):
        return self.doors
    def setDoors(self, ndoors):
        self.doors = ndoors

    def calPrice(self):
        print(f'Final Price of Car {self.price + 50000}')

    def display(self):
        print(f'Doors={self.doors}\t')
        super().display()


class Bus(Vehicle):
    def __init__(self, number1, brand1, price1, seats):
        super().__init__(number1, brand1, price1)
        self.seats = seats

    def getSeats(self):
        return self.seats
    def setSeats(self, nseats):
        self.seats = nseats

    def calPrice(self):
        print(f'Final Price of Bus {self.price + 100000}')

    def display(self):
        print(f'Seats={self.seats}\t')
        super().display()


v1 = Vehicle(101, "Toyota", 500000)
c1 = Car(102, "BMW", 700000, 4)
b1 = Bus(103, "TATA", 900000, 50)

v1.calPrice()
c1.calPrice()
b1.calPrice()
