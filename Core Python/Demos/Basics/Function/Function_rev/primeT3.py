def checkPrime():
    n = int(input("Enter number to check whether it is prime or not: "))

    for i in range(2,n):
        if(n%i==0):
            return False
           
    else:
       return True

result=checkPrime()
print(result)

    

    