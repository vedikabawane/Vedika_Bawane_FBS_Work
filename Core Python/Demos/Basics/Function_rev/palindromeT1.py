def checkPalindrome():
    n = int(input("Check number is palindrome or not: "))

    original = n
    reverse = 0

    while(n > 0):
        d = n % 10
        reverse = reverse * 10 + d
        n = n // 10

    if original == reverse:
        return True
    else:
        return False

print(checkPalindrome())