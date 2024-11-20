def count_vowels_consonents(str):
    vowels='aeiouAEIOU'
    counts={'vowels':0, 'consonenets':0}
    for char in str:
        if char.isalpha():
            if char in vowels:
                counts['vowels']+=1
            else:
                counts['consonenets']+=1

        
    return counts
str=input('enter a string:')
print(count_vowels_consonents(str))