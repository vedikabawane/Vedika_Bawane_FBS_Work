# Write a Program to input two angles from user and find third angle of the triangle. 

#Take input
angle1=int(input('Enter the 1st angle:'))
angle2=int(input('Enter the 2nd angle:'))

#perform operation
#sum of 3 angle is 180
# angle1+angle2+angle3=180

angle3 =180-(angle1 + angle2)

#display
print(f'Third angle of a tringle is {angle3}.')