# num=int(input('Enter number:'))

# for i in range(2,num):
#     if(num%i==0):
#         print(f'{num} is not a prime number.')
#         break
# else:
#     print(f'{num} is prime number.') 



n=int(input('Enter value of n:'))
for n in range(2,n+1):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n, end=' ' )



