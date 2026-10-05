# Write a Python program to remove the intersection of a second set 
# with a first set. 

s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 60, 70}

common = s1.intersection(s2)

for i in common:
    s1.remove(i)

print(s1)