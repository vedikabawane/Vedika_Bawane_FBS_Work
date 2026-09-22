# Write a program to print all numbers which are divisible by m and n in the list

li = [10, 20,33, 45, 93, 66, 13, 29, 25, 47]
m=int(input('Enter number m:'))
n=int(input('Enter number n:'))

new = []

for i in range(len(li)):
    if(li[i] % m == 0 and li[i] % n ==0):
        new = new + [li[i]]

print("Original List:", li)
print("New List:", new)