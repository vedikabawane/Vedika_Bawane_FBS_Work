age1 = int(input('Enter the age of person1: '))
age2 = int(input('Enter the age of person2: '))
age3 = int(input('Enter the age of person3: '))
age4 = int(input('Enter the age of person4: '))
age5 = int(input('Enter the age of person5: '))

ticket = int(input('Enter per person ticket: '))

# Person 1
if age1 < 12:
    A1 = ticket - ticket * 30 / 100
elif age1 > 59:
    A1 = ticket - ticket * 50 / 100
else:
    A1 = ticket

# Person 2
if age2 < 12:
    A2 = ticket - ticket * 30 / 100
elif age2 > 59:
    A2 = ticket - ticket * 50 / 100
else:
    A2 = ticket

# Person 3
if age3 < 12:
    A3 = ticket - ticket * 30 / 100
elif age3 > 59:
    A3 = ticket - ticket * 50 / 100
else:
    A3 = ticket

# Person 4
if age4 < 12:
    A4 = ticket - ticket * 30 / 100
elif age4 > 59:
    A4 = ticket - ticket * 50 / 100
else:
    A4 = ticket

# Person 5
if age5 < 12:
    A5 = ticket - ticket * 30 / 100
elif age5 > 59:
    A5 = ticket - ticket * 50 / 100
else:
    A5 = ticket

Total = A1 + A2 + A3 + A4 + A5

print(f'Total amount of ticket = {Total}')