# WAP to check if a given number is Armstrong number or not.

def checkArmstrongNumber():
    n = int(input('Enter number:'))

    original = n
    count = 0

    while(n > 0):
        count = count + 1
        n = n // 10

    n = original
    sum = 0

    while(n > 0):
        d = n % 10
        n = n // 10
        sum = sum + d ** count

    if(original == sum):
        return 'Number is armstrong.'
    else:
        return 'Number is not armstrong.'

res = checkArmstrongNumber()
print(res)