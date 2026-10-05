# Write a Python program to find the longest common prefix of all 
# strings. Use the Python set. 

li = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(li[0])):
    s = set()

    for j in range(len(li)):
        s.add(li[j][i])

    if len(s) == 1:
        prefix += li[0][i]
    else:
        break

print("Longest common prefix:", prefix)
