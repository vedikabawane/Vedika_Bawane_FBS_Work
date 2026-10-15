# 1. Create a class Book with members as bid,bname,price and author.Add following 
# methods:  
# a. Constructor (Support both parameterized and parameterless)  
# b. Destructor   
# c. ShowBook  
# d. Add static variable count and also maintain count of objects created. 

class Book:
    count = 0  # Static variable to maintain count of objects created

    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1  # Increment count when a new object is created

    def __del__(self):
        print("Book object deleted")
        Book.count -= 1  # Decrement count when an object is deleted
        print(f'Total Books Remaining: {Book.count}')
        
    def showBook(self):
        print(f'Book ID: {self.bid}\tBook Name: {self.bname}\tPrice: {self.price}\tAuthor: {self.author}\tTotal Books: {Book.count}')

b1 = Book(1, "Python Programming", 500, "John Doe")
b1.showBook()
b2 = Book()
b2.showBook()
print(f'Total Books Created: {Book.count}')