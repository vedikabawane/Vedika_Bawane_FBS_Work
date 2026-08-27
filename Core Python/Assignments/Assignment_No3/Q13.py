# Write a program to input electricity unit charges and calculate total electricity bill 
# according to the given condition: 
# For first 50 units Rs. 0.50/unit 
# For next 100 units Rs. 0.75/unit 
# For next 100 units Rs. 1.20/unit 
# For unit above 250 Rs. 1.50/unit 
# An additional surcharge of 20% is added to the bill

units=int(input('Enter the units:'))
if units <= 50:
    bill = units * 0.50

elif units <= 150:
    bill = 50 * 0.50 + (units - 50) * 0.75

elif units <= 250:
    bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20

else:
    bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50

Total_bill=bill*20/100  
Total_electricity_bill=bill+Total_bill 
print(f'total electricity bill is {Total_electricity_bill}.') 




# unit=int(input('Enter the unit:'))

# if(unit<=50):
#     Total=unit*0.50
# elif(unit<=150):
#     Total=unit*0.75
# elif(unit<=250):
#     Total=unit*1.20
# else:
#     Total=unit*1.50

# Total_amount=Total*20/100 
# T=Total+Total_amount
# print(f'Total electricity bill is {T}.')   


