# Write a Python program to find all the unique words and count the 
# frequency of occurrence from a given list of strings. Use Python set 
# data type. 

li = ["apple", "mango", "apple", "banana", "mango"]

unique = set()

for i in li:
    unique.add(i)

for i in unique:
    count = 0

    for j in li:
        if i == j:
            count += 1

    print(i, "=", count)