# WAP to print Armstrong number within a given range 

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):
    temp = num
    sum = 0
    digits = len(str(num))

    while(temp > 0):
        digit = temp % 10
        sum = sum + digit ** digits
        temp = temp // 10

    if(sum == num):
        print(num, end=' ')