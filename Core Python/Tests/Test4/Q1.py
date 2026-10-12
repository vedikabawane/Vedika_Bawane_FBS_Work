# Write a function to which we pass a parameter and
# print the factors of a given number   For Eg: Factors of 12 : 1,2,3,4,6,12

def factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

n = int(input("Enter a number: "))
factors(n)