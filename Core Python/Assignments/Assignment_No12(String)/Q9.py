# Python Program to Calculate the Number of Words and Characters in a String

text = input("Enter string: ")

char_count = 0
word_count = 0

for i in text:
    char_count += 1

    if( i == ' '):
        word_count += 1

if char_count > 0:
    word_count += 1

print("Number of characters:", char_count)
print("Number of words:", word_count)