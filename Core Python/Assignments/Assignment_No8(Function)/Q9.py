# Write a program to check if entered number is a palindrome or 
# not. 

def checkPalindrome():
    n = int(input('Enter number:'))
    original = n
    rev = 0

    while(n > 0):
        d = n % 10
        rev = rev * 10 + d
        n = n // 10

    if(original == rev):
        return 'Number is palindrome.'
    else:
        return 'Number is not palindrome.'

res = checkPalindrome()
print(res)