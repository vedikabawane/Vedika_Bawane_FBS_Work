#  Python Program to count number of digits and letters in a string. 

text = input("Enter string: ")

digit_count = 0
letter_count = 0

for i in text:
    if (i >= 'a' and i <= 'z' or i >= 'A' and i <= 'z'):
        letter_count += 1
    if (i >= '0' and i <= '9'):
        digit_count += 1

print("Number of letter in string :", letter_count)
print("Number of digit in string :", digit_count)