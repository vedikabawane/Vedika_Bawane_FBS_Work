# Write a program to find sum of following series using functions : 
# c. 1^1 + 2^2 + 3^3+ …… n^n 

def sumOfSeries():
    n=int(input('Enter number:'))

    sum=0
    for i in range(1,n+1):
        sum+=i**i
    print(f'Sum of series is {sum}')

sumOfSeries()