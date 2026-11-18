li=[1,3,2,5,8,16]

# newli=[]
# for i in li:
#     if(i%2==0):
#         newli.append('even')
#     else:
#         newli.append('odd')
# print(f"Updated list: {newli}")


newli=['odd' if x%2!=0 else 'even' for x in li]
print(f"Updated list: {newli}")   