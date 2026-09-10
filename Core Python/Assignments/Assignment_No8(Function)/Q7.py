# Write a program to find sum of digits of a number. 

def sumOfDigits():
    n=int(input('Enter number'))

    sum=0

    while(n>0):
        d=n%10
        n=n//10
        sum+=d

    return sum

res=sumOfDigits()
print(res)


