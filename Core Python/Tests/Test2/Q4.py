# Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.

# Input
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))
rate = float(input("Enter painting cost per sq.m: "))

# Area of four walls
area = 2 * (l + b) * h

# Total cost
cost = area * rate

print("Area of four walls:", area, "sq.m")
print("Total cost of painting: Rs.", cost)