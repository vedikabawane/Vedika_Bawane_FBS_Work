
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print((chr(65+j-1)),end=' ')
    for j in range(1,i):
        print((chr(65+j+i-1)),end=' ')
        
    print()