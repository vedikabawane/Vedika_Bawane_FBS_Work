def checkArmstrong(n):

    original = n
    sum = 0

    while(n > 0):
        d = n % 10
        sum = sum + d ** 3
        n = n // 10

    if original == sum:
        return True
    else:
        return False
    
n = int(input("Check number is Armstrong or not: "))
print(checkArmstrong(n))