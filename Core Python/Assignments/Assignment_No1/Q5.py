# Write a program to enter P, T, R and calculate Compound Interest.

#take input
P=int(input('Enter the principle:'))
T=int(input('Enter the time period:'))
R=int(input('Enter the rate interest:'))

#perform operation
C_I=P*(1+R/100)**T-P

#display
print(f'Compound Interast is {C_I}.')