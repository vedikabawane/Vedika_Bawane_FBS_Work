def checkPrime(n):

    for i in range(2,n):
        if(n%i==0):
            return False
           
    return True

n = int(input("Enter number to check whether it is prime or not: "))
result=checkPrime(n)
print(result)

    

    