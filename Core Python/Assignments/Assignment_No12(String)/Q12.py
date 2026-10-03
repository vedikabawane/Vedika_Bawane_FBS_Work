#   Python Program to count number of lowercase characters in a string. 

text = input("Enter string: ")

count = 0

for i in text:
    if (i >= 'a' and i <= 'z'):
        count += 1

print("Number of lowercase characters:", count)