# Write a program to find sum of digits using recursion. 

def sumDigits(n):
    if(n == 0):
        return 0
    else:
        d = n % 10
        return d + sumDigits(n // 10)
n=int(input('Enter number:'))
res=sumDigits(n)
print(res)
