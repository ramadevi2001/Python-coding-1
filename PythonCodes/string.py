str= input('enter a sting:').lower()
if str==str[::-1]:
    print('palindrome')
else:
    print('not a palindome')

#no. of vowels in a string

str= input('enter a sting:').lower()
vowels='aeiouAEIOU'
vowelCount=0
for char in str:
    if char in vowels:
        vowelCount+=1
if vowelCount > 0:
    print(f"The total number of vowels in the string is {vowelCount}.")
else:
    print("There are no vowels in the string.")



