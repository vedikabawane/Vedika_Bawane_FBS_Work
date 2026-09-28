# Print 1 to 100 in Snakes and Ladders pattern

num = 1

for i in range(10):
    if i % 2 == 0:
        for j in range(10):
            print(num, end=' ')
            num += 1
    else:
        num += 9
        for j in range(10):
            print(num, end=' ')
            num -= 1
        num += 11

    print()