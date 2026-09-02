# Write a program to print first n prime numbers.

n = int(input("Enter n: "))

count = 0
num = 2

while(count < n):
    flag = 0

    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

    if(flag == 0):
        print(num, end=' ')
        count += 1

    num += 1