# Write a program to enter P, T, R and calculate simple Interest.

#take input
P=int(input('Enter the principle:'))
T=int(input('Enter the time period:'))
R=int(input('Enter the rate interest:'))

#perform operation
S_I=P*R*T/100

#display
print(f'Simple Interast is {S_I}.')