# b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)  
# 3¹ + 3² + 3³
# = 3 + 9 + 27
# = 39

n=int(input('Enter number:'))

sum=0
for i in range(1,n+1):
    sum=sum+n**i
print(sum)