def num_of_vowels(s):
    vowels='aeiouAEIOU'
    vowel_count=0
    for char in s:
      if char in vowels:
        vowel_count+=1
    return vowel_count
s=input('enter the string:')
print(num_of_vowels(s))

