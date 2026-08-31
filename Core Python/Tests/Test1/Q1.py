# Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:

l=int(input('Enter length:'))
b=int(input('Enter breadth:'))
r=int(input('Enter radius:'))

#area
area_rectangle=l*b
area_circle=3.14*r**2/2
Total_area=area_rectangle+area_circle

#perimeter
P_rectangle=2*(l+b)
C_circle=3.14*r
Total_perimeter=P_rectangle+C_circle

print(f'Total area is {Total_area} & perimeter is {Total_perimeter}')