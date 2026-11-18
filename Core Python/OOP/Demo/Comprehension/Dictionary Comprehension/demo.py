li=[1,3,5,7]

# dict={}
# for i in li:
#     dict[i]=i*i
# print(dict)

# dict={i:i*i for i in range(1,11)}
# print(dict)

dict={i:i*i for i in range(1,11) if(i%2==0)}
print(dict)