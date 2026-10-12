# WAP to print the pattern

width = 20
rows = 10

print("*" * width)

for i in range(rows):
    spaces = 18 - (i * 2)   # decreasing spaces
    if spaces < 0:
        spaces = 0
    print(" " * spaces + "*")

print("*" * width)