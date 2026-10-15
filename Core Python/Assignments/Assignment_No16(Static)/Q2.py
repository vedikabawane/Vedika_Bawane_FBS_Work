# 2. Create a class Product with members as pid,pname,price and quantity .Add 
# following methods:  
# e. Constructor (Support both parameterized and parameterless)  
# f. Destructor   
# g. ShowBook  
# h. Add static member discount.  
# i. Provide methods for applying discount on price of product. 


class Product:
    discount = 0.1  

    def __init__(self, pid=12, pname="laptop", price=50000, quantity=1):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print("Product object deleted")

    def showProduct(self):
        print(f'Product ID: {self.pid}\tProduct Name: {self.pname}\tPrice: {self.price}\tQuantity: {self.quantity}')

    def apply_discount(self):
        self.price *= 1 - Product.discount
        return self.price

p1 = Product(101,"Tablet", 80000, 5)
p1.apply_discount()
p1.showProduct()



    