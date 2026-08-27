# Write a program to swap two numbers without using third variable. 

x=int(input('Enter the first number:'))
y=int(input('Enter the second number:'))
print(f'before swapping x:{x},y:{y}.')
x,y=y,x
print(f'after swapping x:{x},y:{y}.')