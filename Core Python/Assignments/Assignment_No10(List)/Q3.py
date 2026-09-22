# Write a program to find the second largest element in the list. 

li=[10,20,40,60,30,50,70]

max=li[0]
smax=0
for ind in range(1,len(li)):
    if(li[ind]>max):
        smax=max
        max=li[ind]

    elif(li[ind]>smax):
        smax=li[ind]

print('Maximum number', max)
print('Second Maximum number', smax)