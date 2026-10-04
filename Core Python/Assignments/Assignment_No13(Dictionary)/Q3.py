# Python Program to Check if a Given Key Exists in a Dictionary or Not 

di = {1:'Python', 2:'PHP', 3:'Java'}

key = int(input("Enter key: "))

if key in di:
    print("Key exists")
else:
    print("Key does not exist")