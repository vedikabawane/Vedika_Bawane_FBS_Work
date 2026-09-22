# Write a program to create three lists of numbers, their squares 
# and cubes 

li = [1, 2, 3, 4, 6, 8, 9]

square = []
cube=[]

for i in range(len(li)):
    square = square + [li[i] **2]
    cube = cube + [li[i] **3]
    
print('Original list:', li)
print('Square list:', square)
print('Cube list:', cube)