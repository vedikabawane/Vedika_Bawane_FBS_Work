# 1. Create a class Book with members as bid,bname,price and author.Add following 
# methods:  
# a. Constructor (Support both parameterized and parameterless)  
# b. Destructor   
# c. ShowBook  

class Book:
    def __init__(self,bid=None,bname=None,price=None,author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print("Book object deleted")

    def showBook(self):
        print (f'Book ID: {self.bid}\tBook Name: {self.bname}\tPrice: {self.price}\tAuthor: {self.author}')

b1=Book(1,"Python Programming",500,"John Doe")
b1.showBook()
b2=Book()
b2.showBook()