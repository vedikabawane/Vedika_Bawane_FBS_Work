# Python Program to Detect if Two Strings are Anagrams

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) != len(str2):
    print("Not Anagrams")
else:
    found = 1

    for i in range(len(str1)):
        count1 = 0
        count2 = 0

        for j in range(len(str1)):
            if str1[i] == str1[j]:
                count1 += 1

        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count2 += 1

        if count1 != count2:
            found = 0
            break

    if found == 1:
        print("Anagrams")
    else:
        print("Not Anagrams")