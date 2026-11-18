# Write a code to print squre of odd no from list

li=[3,9,10,22,11,7,2,5]

# newli=[]
# for i in li:
#     if (i%2!=0):
#         newli.append(i**2)
# print(f"Updated list: {newli}")

newli=[x**2 for x in li if(x%2!=0)]
print(f"Updated list: {newli}")
        