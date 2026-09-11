# Write a program to check if given number is Armstrong or not
# using recursive function.

def count(n):
    if(n == 0):
        return 0
    else:
        return 1 + count(n // 10)


def armstrong(n, digits):
    if(n == 0):
        return 0
    else:
        d = n % 10
        return d ** digits + armstrong(n // 10, digits)


def checkArmstrongNumber(n):
    digits = count(n)
    sum = armstrong(n, digits)

    if(n == sum):
        return 'Number is armstrong.'
    else:
        return 'Number is not armstrong.'


n = int(input('Enter number:'))
res = checkArmstrongNumber(n)
print(res)