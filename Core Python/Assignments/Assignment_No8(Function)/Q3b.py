# Write a program to find sum of following series using functions : 
# b. 1!+ 2! + 3! + 4!+….. + n! 

def sumOfSeries():
    n = int(input('Enter number: '))

    sum = 0
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
        sum = sum + fact

    print(f'Sum of series is {sum}')

sumOfSeries()
        
