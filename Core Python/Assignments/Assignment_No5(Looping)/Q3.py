#  Accept no. of passengers from user and per ticket cost. Then accept age of each  
# passenger and then calculate total amount to ticket to travel for all of them based on  
# following condition :  
# a. Children below 12 = 30% discount  
# b. Senior citizen (above 59) = 50% discount  
# c. Others need to pay full.


n = int(input("Enter number of passengers: "))
cost = float(input("Enter per ticket cost: "))

total = 0

for i in range(1, n + 1):
    age = int(input("Enter age of passenger: "))

    if (age < 12):
        ticket = cost - (cost * 30 / 100)

    elif (age > 59):
        ticket = cost - (cost * 50 / 100)

    else:
        ticket = cost

    total = total + ticket

print("Total ticket amount =", total)