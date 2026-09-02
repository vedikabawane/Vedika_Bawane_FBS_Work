# Write a program to print prime numbers between 1 to 100. 

n=int(input('Enter value of n:'))

for n in range(2,n+1):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n, end=' ' )
       