# Write a program to check whether a number is prime or not using recursion.

def checkPrime(n, i):
    if(n <= 1):
        return False
    elif(i == n):
        return True
    elif(n % i == 0):
        return False
    else:
        return checkPrime(n, i + 1)


n = int(input('Enter number:'))

res = checkPrime(n, 2)

if(res):
    print('Number is prime.')
else:
    print('Number is not prime.')