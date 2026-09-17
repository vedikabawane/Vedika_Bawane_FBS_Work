li=10,20,40,60,30,50,70

max=li[0]
for ind in range(1,len(li)):
    if(li[ind]>max):
        max=li[ind]

print('Maximum number', max)