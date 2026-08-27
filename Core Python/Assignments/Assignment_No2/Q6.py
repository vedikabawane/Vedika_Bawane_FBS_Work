# WAP to calculate total salary of employee based on basic, da=10% of basic, 
# ta=12% of basic, hra=15% of basic.

basic_salary=int(input('Enter the basic salary of employee:'))

da=basic_salary*10/100
ta=basic_salary*12/100
hra=basic_salary*15/100
total_salary=basic_salary+da+ta+hra

print(f'Total salary of employee is {total_salary}.')