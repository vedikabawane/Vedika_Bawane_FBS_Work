# Write a program to find sum of following series using recursive functions:  
# i. 1! + 2!  + 3! + 4! +….. + n!  
# Note : For fact and sum two recursive functions 

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)


def sum(n):
    if(n == 0):
        return 0
    else:
        return fact(n) + sum(n - 1)


n = int(input('Enter number:'))

res = sum(n)
print('Sum of series:', res)