def checkPerfect(n):

    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum = sum + i

    if sum == n:
        print(True)
    else:
        print(False)


n = int(input("Check number is perfect or not: "))
checkPerfect(n)