# Write a program to reverse the list. 

li= [10,20,30,40,50,60,70]

i = 0
count = 0

# Count number of elements
for x in li:
    count = count + 1

rev = []

i = count - 1

while(i >= 0):
    rev.append(li[i])
    i = i - 1

print('Original list:', li)
print('Reversed list:', rev)
