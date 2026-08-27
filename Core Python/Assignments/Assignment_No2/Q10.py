# Write a program to reverse three-digit number.

num=int(input('Enter 3 digit number:'))

d1=num%10   
num=num//10  
# print(d1)

d2=num%10    
num=num//10   
# print(d2)

d3=num%10  
num=num//10  
# print(d3)

print(f'Reverse of 3 digit number is {d1}{d2}{d3}.')

