# Write a program to accept year from user and check if it is a leap year or not.

year = int(input("Enter year: "))

if (year % 4 == 0):
    print("Leap Year")
elif (year % 100 == 0):
    print("Not a Leap Year")
elif (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
