# Python Program to Merge Two Lists and Sort it 

li1=[20,30,10]
li2=[50,20,30]

merge=[]

for ind in range(len(li1)):
    merge+=[li1[ind]]
for ind in range(len(li2)):
    merge+=[li2[ind]]
print('After merging:',merge)

size=len(merge)
for i in range(1,size):
        for j in range(0,size-i):
            if(merge[j]>merge[j+1]):
                merge[j], merge[j+1] = merge[j+1], merge[j]

print('After sorting:',merge)