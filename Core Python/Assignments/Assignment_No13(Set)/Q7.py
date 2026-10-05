# Given two sets of numbers, write a Python program to find the missing 
# numbers in the second set as compared to the first and vice versa. 
# Use the Python set. 

s1={10,20,30,40}
s2={30,40,50,60}
print(s1.symmetric_difference(s2))