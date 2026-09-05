def checkPrime():
    n=int(input('Enter number:'))

    for i in range(2,n):
        if(n%i==0):
            print(False)
            print('It is not prime number')
            break
    else:
        print(True)
        print('It is prime number')

checkPrime()
    

    