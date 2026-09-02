#  Write a program to check if given 3 digit number is a palindrome or not. 

num=int(input('Enter 3 digite number: '))

a=num//100
b=(num//10)%10
c=num%10

reverse=c*100+b*10+a

if(num==reverse):
    print('Number is a palindrome.')
else:
    print('Number is a not palindrome.')
    

