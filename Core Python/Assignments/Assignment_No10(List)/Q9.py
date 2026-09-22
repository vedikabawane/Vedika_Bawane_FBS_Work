# Write a program of having n number of elements in the list and find out even 
# and odd elements in that list and then create two separate lists which will have 
# even elements and other will have odd elements. 

li = [10, 20, 33, 45, 22, 76, 43, 93]

even = []
odd=[]

for i in range(len(li)):
    if(li[i] % 2 == 0):
        even = even + [li[i]]
    else:
        odd = odd + [li[i]]

print("Original List:", li)
print("Even List:", even)
print("Odd List:", odd)