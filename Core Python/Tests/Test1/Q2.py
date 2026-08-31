# Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)

P=int(input('Enter principal:'))
R=int(input('Enter rate:'))
T=int(input('Enter time:'))

SI=P*R*T/100

print(f'Simple intrest is {SI}.')