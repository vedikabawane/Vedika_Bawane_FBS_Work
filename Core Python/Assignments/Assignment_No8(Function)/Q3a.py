# Write a program to find sum of following series using functions : 
# a.  1+ 2 + 3 + 4+….. + n 

def sumOfSeries():
    n=int(input('Enter number:'))

    sum=0
    for i in range(1,n+1):
        sum+=i
    print(f'Sum of series is {sum}')

sumOfSeries()