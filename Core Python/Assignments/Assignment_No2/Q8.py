# Write a program to swap two numbers using third variable. 

x=int(input('Enter the first number:'))
y=int(input('Enter the second number:'))
print(f'before swapping x:{x},y:{y}.')
z=y
y=x
x=z
print(f'after swapping x:{x},y:{y}.')