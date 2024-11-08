str1=input('enter string:')
str2=input('enter string: ')

str1=str1.replace(' ','').lower() # removing the spaces and change it to lowercase
str2=str2.replace(' ','').lower()
result=sorted(str1)==sorted(str2)
if result is True:
    print('the strings are anagrams')
else:
    print('not anagrams')