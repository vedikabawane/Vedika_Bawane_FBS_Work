# Python Program to Count the Frequency of Words Appearing in a String Using 
# a Dictionary 
 
text = input("Enter string: ")

di = {}
word = ""

for i in text:
    if i != ' ':
        word += i
    else:
        if word != '':
            if word in di:
                di[word] += 1
            else:
                di[word] = 1
            word = ''

if word != '':
    if word in di:
        di[word] += 1
    else:
        di[word] = 1

print(di)