def palindrome(str):
    str=str.lower()
    filtered_str=''.join(char for char in str if char.isalnum())
    return filtered_str == filtered_str[::-1]
str=input('enter a string:')
print(palindrome(str))

'''
filtered_string = ''.join(char for char in string if char.isalnum())
This is a generator expression inside a join() method, which builds a new string that contains only the alphanumeric 
characters from the input string.
'''