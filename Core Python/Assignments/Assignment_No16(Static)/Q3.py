# 2. Create a class Product with members as pid,pname,price and quantity .Add 
# following methods:  
# e. Constructor (Support both parameterized and parameterless)  
# f. Destructor   
# g. ShowBook  
# h. Add static member discount.  
# i. Provide methods for applying discount on price of product.  

class Product:
    discount = 10  # static member in percentage

    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print(f"Product object with ID {self.pid} is deleted.")

    def showProduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def apply_discount(self):
        self.price = self.price - (self.price * Product.discount / 100)
        print(f"Discounted price: {self.price}")

# Parameterless constructor
p1 = Product()
p1.pid = 101
p1.pname = "Laptop"
p1.price = 50000
p1.quantity = 2
p1.showProduct()
p1.apply_discount()

print()

# Parameterized constructor
p2 = Product(102, "Mobile", 20000, 5)
p2.showProduct()
p2.apply_discount()