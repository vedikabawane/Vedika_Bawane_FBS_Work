
# Write a program to print list after removing even numbers.

li = [10, 20, 30, 13, 30, 45, 64, 50]

new = []

for i in range(len(li)):
    if(li[i] % 2 != 0):
        new = new + [li[i]]

print(new)