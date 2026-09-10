# Write a program find reverse of a number 

def revOfNumber():
    n=int(input('Enter number:'))
    
    while(n>0):
        d=n%10
        n=n//10
    return d
res=revOfNumber()
print(res)