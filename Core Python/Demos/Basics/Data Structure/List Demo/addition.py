li=10,20,30,40,50,60,70

sum=0

#method 1: Iterating values
for ele in li:
    # print(ele)
    sum+=ele 

#method 2 : Using indexing
for ind in range(0, len(li)):
    # print(ind)
    sum+=li[ind]

print(sum)