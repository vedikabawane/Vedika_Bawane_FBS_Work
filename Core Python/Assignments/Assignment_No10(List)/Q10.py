# Write a program to remove all occurrences of a given element in the list.


li = [10, 20, 30, 40, 50]
n=int(input('Enter number:'))

new = []

for i in range(len(li)):
    if(li[i] != n):
        new = new + [li[i]]

print("Original List:", li)
print("New List:", new)