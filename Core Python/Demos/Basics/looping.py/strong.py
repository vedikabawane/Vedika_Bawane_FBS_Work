num=int(input('Enter number:'))

temp=num
sum=0

while(temp>0):
    d=temp%10
    temp=temp//10
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact

if(sum==num):
    print('The number is strong')
else:
    print('The number is not strong')
