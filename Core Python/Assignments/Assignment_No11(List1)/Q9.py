# 9. Write a program to create three lists of numbers, their squares and cubes 

li=[1,2,3,4,5,6]

squares=[]
cubes=[]

for ind in range(1,len(li)):
    squares+=[li[ind]**2]
    cubes+=[li[ind]**3]

print(squares)
print(cubes)

