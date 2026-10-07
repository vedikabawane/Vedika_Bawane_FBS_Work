class Animal:
    def __init__(self, name1, age1, color1):
        self.name = name1
        self.age = age1
        self.color = color1

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getAge(self):
        return self.age
    def setAge(self, newage):
        self.age = newage

    def getColor(self):
        return self.color
    def setColor(self, newcolor):
        self.color = newcolor

    def display(self):
        print(f"Name={self.name}\tAge={self.age}\tColor={self.color}")


class PetAnimal(Animal):
    def __init__(self, name1, age1, color1, owner):
        super().__init__(name1, age1, color1)
        self.owner = owner
    def getOwner(self):
        return self.owner
    def setOwner(self, newowner):
        self.owner = newowner
    def display(self):
        print(f"Owner={self.owner}\t")
        super().display()


class WildAnimal(Animal):
    def __init__(self, name1, age1, color1, habitat):
        super().__init__(name1, age1, color1)
        self.habitat = habitat
    def getHabitat(self):
        return self.habitat
    def setHabitat(self, newhabitat):
        self.habitat = newhabitat
    def display(self):
        print(f"Habitat={self.habitat}\t")
        super().display()


a1 = Animal("Animal", 5, "Brown")
p1 = PetAnimal("Dog", 3, "Black", "Vedika")
w1 = WildAnimal("Tiger", 6, "Orange", "Forest")

a1.display()
p1.display()
w1.display()