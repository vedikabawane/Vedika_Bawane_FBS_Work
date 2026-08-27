x=10
y=10
z=20
li1=[10,20]
li2=[10,20]


#mutable  -can change
#can't reuse

#immutable  -can't change
#can reuse

#1.is
print(x is y)
print(li1 is li2)
print(id(x))
print(id(y))
print(id(li1))
print(id(li2))

#2is not
print(x is not y)
print(li1 is not li2)