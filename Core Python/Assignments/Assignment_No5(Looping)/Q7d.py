# S = a + a2 / 2 + a3 / 3 + …… + a10 / 10 

a=int(input('Enter number:'))
sum=0
for i in range(1,11):
    s=a**i/i
    sum=sum+s
print(sum)
