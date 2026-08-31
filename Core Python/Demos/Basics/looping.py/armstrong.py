num=int(input('Enter number:'))

temp=num
count=0
while(temp>0):
    count+=1
    temp=temp//10
# print(count)

sum=0
temp=num
while(temp>0):
    d=temp%10
    temp=temp//10
    sum=sum+(d**count)

if(sum==num):
    print(f'{num} is a armstrong number.')
else:
    print(f'{num} is a not armstrong number.')


