# Python Program to Remove the nth Index Character from a Non-Empty 
# String 

text = input('Enter String: ')
n = int(input('Enter index: '))

new = ''

for i in range(len(text)):
    if (i != n):
        new += text[i]

print(new)