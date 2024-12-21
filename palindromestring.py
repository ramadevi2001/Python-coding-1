def palindrome(str):
    if str == str[::-1]:
        return 'palindrome'
    else:
        return 'not palindome'
str = input('enter a str:').lower()
print(palindrome(str))