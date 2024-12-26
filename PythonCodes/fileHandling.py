with open('devi.txt','w') as file:
    file.write('Hello devi how are you')
    print(file)
with open('devi.txt','r') as file:
    content=file.read()
    print(content)

# read from the file and count the number of words in it

with open('devi.txt','r') as file:
    content = file.read()
    words = content.split()
    letters=[char for char in content if char.isalpha()]
    letter_count=len(letters)
    word_count=len(words)
    print(word_count)
    print(letter_count)

# append to the file

with open('devi.txt','a') as file:
    file.write('\n' + 'I am cheruku Rama devi how are you')

# count occurence of words in file
from collections import Counter
with open('devi.txt','r') as file:
    content=file.read()
    words=content.split()
    word_count=Counter(words)
for word,count in word_count.items():
    print(word,':',count)


