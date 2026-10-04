# Python Program to Remove the Given Key from a Dictionary 

di = {1:'Python', 2:'PHP', 3:'Java'}
key=int(input('Enter key:'))


if key in di:
    di.pop(key)
    print(di)
else:
    print('Key not found')
