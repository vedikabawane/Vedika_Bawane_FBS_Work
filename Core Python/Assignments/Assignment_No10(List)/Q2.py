# Write a program to find maximum and minimum element in a list. 

li=[10,20,40,60,30,50,70]

max=li[0]
for ind in range(1,len(li)):
    if(li[ind]>max):
        max=li[ind]

print('Maximum number', max)

min=li[0]
for ind in range(1,len(li)):
    if(li[ind]<min):
        min=li[ind]

print('Minimum number', min)