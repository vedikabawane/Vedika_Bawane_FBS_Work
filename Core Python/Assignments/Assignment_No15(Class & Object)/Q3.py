# Create a class Shirt  with members as sid,sname,type(formal etc), price and 
# size(small,large etc) .Add following methods:  
# ShowBook  
# g. Constructor (Support both parameterized and parameterless)  
# h. Destructor  
# i. ShowBook  

class Shirt:
    def __init__(self,sid=None,sname=None,type=None,price=None,size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("Shirt object deleted")

    def showShirt(self):
        print (f'Shirt ID: {self.sid}\tShirt Name: {self.sname}\tType: {self.type}\tPrice: {self.price}\tSize: {self.size}')

s1=Shirt(201,"Formal Shirt","Formal",1500,"Large")
s1.showShirt()
s2=Shirt()
s2.showShirt()