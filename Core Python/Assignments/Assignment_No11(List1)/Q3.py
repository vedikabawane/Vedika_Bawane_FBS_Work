# Python Program to Sort the List According to the Second Element in Sublist

li = [[10, 30], [20, 10], [40, 20], [50, 5]]

size = len(li)

for i in range(1, size):
    for j in range(0, size-i):
        if li[j][1] > li[j+1][1]:
            li[j], li[j+1] = li[j+1], li[j]

print("After sorting:", li)