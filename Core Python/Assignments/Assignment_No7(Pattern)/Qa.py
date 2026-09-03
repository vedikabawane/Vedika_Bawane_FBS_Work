for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')

    print('*',end=' ')

    if i > 1:
        for j in range(1,2*i-2):
            print(' ',end=' ')

        print('*',end=' ')

    print()