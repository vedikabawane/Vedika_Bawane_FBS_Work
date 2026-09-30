# Write a program to print list after removing even numbers. 

li=[10,11,33,23,45,67,88,28,29,36]

even=[]
for i in range(1,len(li)):
    if(li[i] % 2 != 0):
        even = even + [li[i]]
print('Afer removing even number:',even)

