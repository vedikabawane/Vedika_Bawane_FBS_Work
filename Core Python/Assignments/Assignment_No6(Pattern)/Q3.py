for i in range(4):
    num = 1

    for j in range(4 - i):
        print(' ', end=' ')

    for j in range(i + 1):
        print(num, end='   ')
        num = num * (i - j) // (j + 1)

    print()