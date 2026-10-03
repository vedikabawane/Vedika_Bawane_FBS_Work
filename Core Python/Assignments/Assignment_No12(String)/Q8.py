# Python Program to Remove the Characters of Odd Index Values in a 
# String 

str=input('Enter string:')

new=' '
for i in range(len(str)):
    if(i % 2 == 0):
        new+=str[i]
print(new)

