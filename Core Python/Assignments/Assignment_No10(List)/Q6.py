# Write a program to remove duplicates from the list. 

li = [10, 20, 30, 10, 30, 40, 60, 50]

new = []
size = 0

for i in range(len(li)):
    found = 0

    for j in range(size):
        if(li[i] == new[j]):
            found = 1
            break

    if(found == 0):
        new = new + [li[i]]
        size = size + 1

print(new)
