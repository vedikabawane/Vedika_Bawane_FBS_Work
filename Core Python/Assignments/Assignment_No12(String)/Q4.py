# Python Program to Form a New String where the First Character and 
# the Last Character have been Exchanged 

str=input('Enter String:')

first=str[0]
last=str[len(str)-1]
middle=str[1:len(str)-1]

new = str[len(str)-1] + str[1:len(str)-1] + str[0]

new=last+middle+first
print(new)