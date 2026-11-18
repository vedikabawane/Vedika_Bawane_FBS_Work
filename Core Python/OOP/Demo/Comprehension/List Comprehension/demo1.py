#Write a program to add 10 in each element of list

li=[10,1,20,11,13,14]

# newli=[]
# for i in li:
#     newli.append(i + 10)
# print(f"Updated list: {newli}")

newli=[x+10 for x in li]
print(f"Updated list=",newli)
