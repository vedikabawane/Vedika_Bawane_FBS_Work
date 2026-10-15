# 2. Create a class Product with members as pid,pname,price and quantity .Add 
# following methods:  
# d. Constructor (Support both parameterized and parameterless)  
# e. Destructor   
# f. ShowBook  

class Product:
    def __init__(self,pid=None,pname=None,price=None,quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print("Product object deleted")

    def showProduct(self):
        print (f'Product ID: {self.pid}\tProduct Name: {self.pname}\tPrice: {self.price}\tQuantity: {self.quantity}')

p1=Product(101,"Laptop",80000,5)
p1.showProduct()
p2=Product()
p2.showProduct()
