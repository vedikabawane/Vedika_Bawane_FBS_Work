# Python Program to Put Even and Odd elements of a List into two Different 
# Lists 

li = [10, 20, 30, 13, 30, 45, 64, 50]

even = []
odd=[]

for i in range(len(li)):
    if(li[i] % 2 == 0):
        even = even + [li[i]]
    else:
        odd = odd + [li[i]]

print('Original list:',li)
print('Even list:',even)
print('Odd list:',odd)