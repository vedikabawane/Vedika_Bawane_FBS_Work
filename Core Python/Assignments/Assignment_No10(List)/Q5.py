# Accept a number from user and check if this element is present in the list or 
# not. Also tell how many times it is present in the list. 

n = int(input('Enter number:'))

li = [10,20,30,10,30,40,60,50]

count = 0

for i in range(len(li)):
    if(n == li[i]):
        count += 1

if(count > 0):
    print('Number is present')
    print(f'It is present {count} times.')
else:
    print('Number is not present.')
