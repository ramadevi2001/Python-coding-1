def frequencyofwordcount(str):
    str="apple banana apple orange banana apple"
    word_count=str.split()
    frequency={}
    for word in word_count:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    return frequency
print(frequencyofwordcount(str))

# using counter from collections
from collections import Counter
str= "apple banana apple orange banana apple"
word_count=Counter(str.split())
print(dict(word_count))
