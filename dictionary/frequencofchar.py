def frequencyofchar(str):
    char_frequency={}
    for char in str:
        if char in char_frequency:
            char_frequency[char]+=1
        else:
            char_frequency[char]=1
    return char_frequency
str='hello'
print(frequencyofchar(str))

# using collection counter
from collections import Counter
str='devi'
char_frequency=Counter(str)
print(dict(char_frequency))