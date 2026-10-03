#  Python Program to count the occurrences of each word in a string.

text = input("Enter string: ")
word = input("Enter word: ")

count = 0
current = ""

for i in text:
    if i != ' ':
        current += i
    else:
        if current == word:
            count += 1
        current = ''

if current == word:
    count += 1

print("Occurrence of", word, ":", count)