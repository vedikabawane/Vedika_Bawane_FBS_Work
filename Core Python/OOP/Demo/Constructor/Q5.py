class Movie:
    def __init__(self, name1, language1, rating1):
        self.name = name1
        self.language = language1
        self.rating = rating1

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getLanguage(self):
        return self.language
    def setLanguage(self, newlanguage):
        self.language = newlanguage

    def getRating(self):
        return self.rating
    def setRating(self, newrating):
        self.rating = newrating

    def display(self):
        print(f"Name={self.name}\tLanguage={self.language}\tRating={self.rating}")


p1 = Movie("Movie A", "Hindi", 4.5)
p2 = Movie("Movie B", "English", 4.0)

p1.display()
p2.display()

p2.setRating(4.5)
p2.display()