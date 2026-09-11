# Write a program to check if entered year is a leap year or not.

def checkYear():
    year = int(input('Enter year:'))

    if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        return 'Leap year'
    else:
        return 'Not leap year'

res = checkYear()
print(res)