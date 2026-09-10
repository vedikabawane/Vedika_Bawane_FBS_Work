# Write a program to find print the following Fibonacci series using 
# functions: 
# 1  1  2  3 5 8  n terms

def fibonacciSeries():
    n=int(input('Enter number:'))
    a=1
    b=0
    for i in range(n):
        c=a+b
        print(c,end=' ')
        a=b
        b=c

fibonacciSeries()