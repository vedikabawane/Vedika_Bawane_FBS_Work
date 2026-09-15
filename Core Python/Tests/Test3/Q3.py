# Write a program to accept basic salary of n employees.
# If basic salary is below 20000:
# DA = 10%, TA = 12%, HRA = 15%
# Otherwise:
# DA = 15%, TA = 18%, HRA = 20%

n = int(input('Enter number of employees: '))

total_salary = 0

for i in range(1, n + 1):

    basic = float(input('Enter basic salary of employee: '))

    if(basic < 20000):
        da = basic * 10 / 100
        ta = basic * 12 / 100
        hra = basic * 15 / 100
    else:
        da = basic * 15 / 100
        ta = basic * 18 / 100
        hra = basic * 20 / 100

    salary = basic + da + ta + hra

    print('Total salary of employee', i, ':', salary)

    total_salary = total_salary + salary

print('Total salary of all employees:', total_salary)