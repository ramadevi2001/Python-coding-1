def reverse_words(str):
    words=str.split()
    reversed_words=words[::-1]
    reversed_str=' '.join(reversed_words)
    return reversed_str
str= input('enter a sentece:')
print(reverse_words(str))
