#  Python Program to find larger string without using built-in functions. 

str1 = input('Enter string: ')
str2 = input('Enter string: ')

count_str1 = 0
count_str2 = 0

for i in str1:
    count_str1 += 1

for i in str2:
    count_str2 += 1

if (count_str1 > count_str2):
    print(str1)
elif( count_str2 > count_str1):
    print(str2)
else:
    print("Both strings are equal in length")
