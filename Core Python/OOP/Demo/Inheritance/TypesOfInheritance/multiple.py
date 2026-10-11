class Electronics:
    def display(self):
        print("Electronics")

class Mechanical:
    def display(self):
        print("Mechanical")

class Mechatronics(Electronics,Mechanical):
    def display(self):
        print("Mechatronics")

m=Mechatronics()
m.display()