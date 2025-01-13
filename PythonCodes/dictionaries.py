# find the frequencies of characters in string

def frequciesOfCharacters(str):
    frequencies={}
    for char in str:
        if char in frequencies:
            frequencies[char]+=1
        else:
            frequencies[char]=1
    return frequencies
str= input('enter a string:')
print(f'Frequencies of characters in a string are: \n {frequciesOfCharacters(str)}')

# merge two dictionaries

dict1=eval(input('enter dict1:'))
dict2=eval(input('enter dict2:'))
dict1.update(dict2)
print(dict1)