def checkPrime(n):

    for i in range(2,n):
        if(n%i==0):
            print(False)
            print('Number is not prime number.')
            break
    else:
        print(True)
        print('Number is prime number.')

n=int(input('Enter number:'))
checkPrime(n)
    

    