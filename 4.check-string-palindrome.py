def palindrome(s):
    
    if s == s[::-1]:
        return f"{s}: is palindrome "
    else:
        return 'not a palindrome'
s= input('enter a string:').lower()
print(palindrome(s))