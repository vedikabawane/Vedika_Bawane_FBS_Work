# Write a Python program to find all the anagrams and group them 
# together from a given list of strings. 

li = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = []
used = set()

for i in range(len(li)):
    if li[i] in used:
        continue

    group = [li[i]]
    used.add(li[i])

    for j in range(i + 1, len(li)):
        if len(li[i]) == len(li[j]):

            count = 0

            for k in range(len(li[i])):
                for l in range(len(li[j])):
                    if li[i][k] == li[j][l]:
                        count += 1
                        break

            if count == len(li[i]):
                group.append(li[j])
                used.add(li[j])

    groups.append(group)

print(groups)