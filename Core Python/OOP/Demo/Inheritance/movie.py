class Movie:
    def __init__(self, movieid1, name1, price1):
        self.movieid = movieid1
        self.name = name1
        self.price = price1

    def getMovieId(self):
        return self.movieid
    def setMovieId(self, newmovieid):
        self.movieid = newmovieid

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getPrice(self):
        return self.price
    def setPrice(self, newprice):
        self.price = newprice
        
    def display(self):
        print(f"Movie Id={self.movieid}\tName={self.name}\tPrice={self.price}")


class BollywoodMovie(Movie):
    def __init__(self, movieid1, name1, price1, language):
        super().__init__(movieid1, name1, price1)
        self.language = language
    def getLanguage(self):
        return self.language
    def setLanguage(self, nlanguage):
        self.language = nlanguage
    def display(self):
        print(f"Language={self.language}\t")
        super().display()


class HollywoodMovie(Movie):
    def __init__(self, movieid1, name1, price1, language):
        super().__init__(movieid1, name1, price1)
        self.language = language
    def getLanguage(self):
        return self.language
    def setLanguage(self, nlanguage):
        self.language = nlanguage
    def display(self):
        print(f"Language={self.language}\t")
        super().display()


m1 = Movie(101, "General Movie", 200)
b1 = BollywoodMovie(102, "Dangal", 250, "Hindi")
h1 = HollywoodMovie(103, "Avatar", 300, "English")

m1.display()
b1.display()
h1.display()