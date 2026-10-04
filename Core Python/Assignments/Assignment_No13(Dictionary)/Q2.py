# Python Program to Concatenate Two Dictionaries Into One 

di1={1:'Python',2:'PHP',3:'Java'}
di2={'Name':'Vedika','Add':'Warora'}
new={}

for i in di1:
    new[i]=di1[i]

for i in di2:
    new[i]=di2[i]

print(new)

