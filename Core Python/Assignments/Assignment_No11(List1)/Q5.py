# Python Program to Sort a List According to the Length of the Elements 
# within the list. 

# Python Program to Sort a List According to the Length of the Elements

li = ["apple", "cat", "banana", "hi", "elephant"]

size = len(li)

for i in range(1, size):
    for j in range(0, size-i):
        if len(li[j]) > len(li[j+1]):
            li[j], li[j+1] = li[j+1], li[j]

print("After sorting:", li)