# Write a program to calculate profit or loss.

SP=int(input('Enter the selling price:'))
CP=int(input('Enter the cost price:'))

if(SP>CP):
    profit=SP-CP
    print(f'Profit is {profit}.')
elif(CP>SP):
    loss=CP-SP
    print(f'Loss is {loss}.')
else:
    print('No profit or loss.')  