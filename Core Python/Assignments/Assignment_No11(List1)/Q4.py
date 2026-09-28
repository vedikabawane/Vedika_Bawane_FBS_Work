# Python Program to Find the Second Largest Number in a List Using Bubble Sort 

li=[20,50,80,90,50,40]

size = len(li)

for i in range(1, size):
    for j in range(0, size-i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

print("After sorting:", li)
print("Second largest:", li[size-2])