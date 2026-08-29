# WAP to print all numbers in a range divisible by a given number.  

start=int(input('Enter starting of range:'))
end=int(input('Enter ending of range:'))
n=int(input('Enter given number:'))

for i in range(start,end+1):  
    if(i%n==0):
        print(i,end=' ')