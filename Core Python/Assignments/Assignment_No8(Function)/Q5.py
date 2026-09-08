# Sum of all prime numbers between 1 to n 

def sumOfPrime():
    n = int(input('Enter number: '))

    sum = 0

    for num in range(2, n + 1):
        for i in range(2, num):
            if(num % i == 0):
                break
        else:
            sum = sum + num

    print(f'Sum of prime numbers is {sum}')

sumOfPrime()
