# Write a program to reverse a given number using recursive function.

def reverse(n, rev):
    if(n == 0):
        return rev
    else:
        d = n % 10
        rev = rev * 10 + d
        return reverse(n // 10, rev)

n = int(input('Enter number:'))

res = reverse(n, 0)
print('Reverse number:', res)