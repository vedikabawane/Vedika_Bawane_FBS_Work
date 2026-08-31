# Calculate the cost of painting the following building’s walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and
# exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)

area=int(input('Enter the one wall area:'))
I_cost=int(input('Enter cost of interior per wall:'))
E_cost=int(input('Enter cost of exterior per wall:'))

I=area*I_cost*6
E=area*E_cost*3
Total_cost=I+E

print(f'Cost of building painting is {Total_cost}.')