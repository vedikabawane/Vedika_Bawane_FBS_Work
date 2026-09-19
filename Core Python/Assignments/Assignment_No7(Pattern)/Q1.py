for i in range(10):

    if(i <= 4):
        space = 4 - i
        gap = 2 * i - 1
    else:
        space = i - 5
        gap = 2 * (9 - i) - 1

    for j in range(space):
        print(' ', end=' ')

    print('*', end='')

    if(i != 0 and i != 9):
        for j in range(gap):
            print(' ', end=' ')
        print('*', end='')

    print()