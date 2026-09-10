# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

# Given values
r = 20
l = 50
b = 40
cost = 35

# Perimeter of semicircle
semi_circle = 3.14 * r

# Perimeter of rectangle
rectangle = 2 * (l + b)

# Total perimeter
perimeter = semi_circle + rectangle

# Fencing 5 times
total_wire = perimeter * 5

# Total cost
total_cost = total_wire * cost

print("Total wire required:", total_wire, "m")
print("Total cost of fencing: Rs.", total_cost)