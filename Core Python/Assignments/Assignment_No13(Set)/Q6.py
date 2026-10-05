# Write a Python program to find the two numbers whose product is 
# maximum among all the pairs in a given list of numbers. Use the 
# Python set. 

li = [2, 5, 3, 8, 4]

pair = set()

for i in range(len(li)):
    for j in range(i+1, len(li)):
        pair.add((li[i], li[j]))

max_product = 0
max_pair = ()

for p in pair:
    product = p[0] * p[1]

    if product > max_product:
        max_product = product
        max_pair = p

print("Pair:", max_pair)
print("Maximum product:", max_product)