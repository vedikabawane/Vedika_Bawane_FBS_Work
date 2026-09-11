data=[1,2,3,4,5,6,7,8,9,10]

# res=list(filter(lambda n: n*n,data))
res=tuple(filter(lambda num: num%2==0,data))

print(res)
