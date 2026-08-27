# Write a program to input all sides of a triangle and check whether triangle is valid or 
# not. 

a=int(input('Enter the side1:'))
b=int(input('Enter the side2:'))
c=int(input('Enter the side3:'))

if(a+b>c and a+c>b and b+c>a):
    print('Triangle is valid')
else:
    print('Triangle is not valid')   