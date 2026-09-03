# e. x - x2/3 + x3/5 - x4/7 + …. to n terms  

x=int(input('Enter x:'))
n=int(input('Enter number:'))

sum=0
for i in range(1,n+1):
    term = x**i / (2*i-1)
    if(i%2==0):
        sum=sum-term
    else:
        sum=sum+term
print(sum,end=' ')