# Write a program to convert days into years, weeks and days. 

days = int(input("Enter number of days: "))

years = days // 365
remaining_days = days % 365

weeks = remaining_days // 7
days = remaining_days % 7

# print("Years =", years)
# print("Weeks =", weeks)
# print("Days =", days)

#display
print(f'Years:{years} , Weeks:{weeks} , Days:{days}.')