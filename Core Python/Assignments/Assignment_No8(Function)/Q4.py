# Sum of all odd numbers between 1 to n

def OddNumber():
    n=int(input('Enter number:'))

    for i in range(1,n+1):
        if(i%2!=0):
            print(i,end=' ')
    print()

OddNumber()

