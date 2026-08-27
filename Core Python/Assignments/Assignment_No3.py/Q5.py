# Write a program to check whether the triangle is equilateral, isosceles or scalene 
# triangle. 

a=int(input('Enter the side1:'))
b=int(input('Enter the side2:'))
c=int(input('Enter the side3:'))

if(a==b==c):
    print('It is equilateral triangle.')
elif(a == b or b == c or a == c):
    print('It is isosceles triangle.')
elif(a != b and b != c and a != c):
    print('It is scalene triangle.')