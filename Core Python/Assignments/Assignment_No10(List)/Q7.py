# Write a program to create a new list from existing list which contains cube of 
# each number of list. 

li = [1, 2, 3, 4, 6, 8, 9]

new = []

for i in range(len(li)):
    new = new + [li[i] **3]
print(new)
