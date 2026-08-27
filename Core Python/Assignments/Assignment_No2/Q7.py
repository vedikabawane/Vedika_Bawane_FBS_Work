# Find the sum of three-digit number. 

num=int(input('Enter 3 digit number:'))

d1=num%10   
num=num//10  
# print(d1)

d2=num%10    
num=num//10   
# print(d2)

d3=num%10  
num=num//10  
# print(d3)
# print(f'd1:{d1},d2:{d2},d3:{d3},')

sum_of_three_digit_number=d1+d2+d3
print(f'sum of three digit number is {sum_of_three_digit_number}.')