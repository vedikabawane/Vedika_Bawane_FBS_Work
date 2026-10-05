#  Write a Python program to find all the unique combinations of 3 
# numbers from a given list of numbers, adding up to a target number. 

li = [2, 4, 6, 8, 10]
target = 18

for i in range(len(li)):
    for j in range(i+1,len(li)):
        for k in range(j+1,len(li)):
            sum = li[i] + li[j] + li[k]
            
            if(sum==target):
                print(li[i],li[j],li[k])