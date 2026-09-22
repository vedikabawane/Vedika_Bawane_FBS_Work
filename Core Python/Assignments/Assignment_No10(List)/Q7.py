# Write a program to create a new list from existing list which contains cube of 
# each number of list. 

li = [1, 2, 3, 4, 6, 8, 9]

new = [0] * len(li)

i = 0

for num in li:
    new[i] = num ** 3
    i = i + 1

print(new)
