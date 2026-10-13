
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

    def calPrice(self):
        print(f'Final Price of Movie {self.price}')

    def display(self):
        print(f"Movie Id={self.movieid}\tName={self.name}\tPrice={self.price}")


class BollywoodMovie(Movie):
    def __init__(self, movieid1, name1, price1, tax):
        super().__init__(movieid1, name1, price1)
        self.tax = tax

    def getTax(self):
        return self.tax
    def setTax(self, ntax):
        self.tax = ntax

    def calPrice(self):
        print(f'Final Price of Bollywood Movie {self.price + self.tax}')

    def display(self):
        print(f'Tax={self.tax}\t')
        super().display()


class HollywoodMovie(Movie):
    def __init__(self, movieid1, name1, price1, charge):
        super().__init__(movieid1, name1, price1)
        self.charge = charge

    def getCharge(self):
        return self.charge
    def setCharge(self, ncharge):
        self.charge = ncharge

    def calPrice(self):
        print(f'Final Price of Hollywood Movie {self.price + self.charge}')

    def display(self):
        print(f'Charge={self.charge}\t')
        super().display()


m1 = Movie(101, "General Movie", 200)
b1 = BollywoodMovie(102, "Dangal", 250, 50)
h1 = HollywoodMovie(103, "Avatar", 300, 100)

m1.calPrice()
b1.calPrice()
h1.calPrice()
