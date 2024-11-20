def First_non_repeating_character(str):
    char_count={}
    for char in str:
        char_count[char]= char_count.get(char,0) +1
    for char in str:
        if char_count[char]==1:
            return char
    return None
str=input('enter a str:')
print(First_non_repeating_character(str))

'''
Let’s go through an example with s = "swiss":

At the start, char_count = {} (an empty dictionary).

First Iteration (char = 's'):

char_count.get('s', 0) → 0 (since 's' is not in char_count yet).
char_count['s'] = 0 + 1 → 1.
Now, char_count = {'s': 1}.
Second Iteration (char = 'w'):

char_count.get('w', 0) → 0 (since 'w' is not in char_count yet).
char_count['w'] = 0 + 1 → 1.
Now, char_count = {'s': 1, 'w': 1}.
Third Iteration (char = 'i'):

char_count.get('i', 0) → 0 (since 'i' is not in char_count yet).
char_count['i'] = 0 + 1 → 1.
Now, char_count = {'s': 1, 'w': 1, 'i': 1}.
Fourth Iteration (char = 's'):

char_count.get('s', 0) → 1 (since 's' is already in char_count with a count of 1).
char_count['s'] = 1 + 1 → 2.
Now, char_count = {'s': 2, 'w': 1, 'i': 1}.
Fifth Iteration (char = 's' again):

char_count.get('s', 0) → 2 (since 's' is already in char_count with a count of 2).
char_count['s'] = 2 + 1 → 3.
Now, char_count = {'s': 3, 'w': 1, 'i': 1}.
'''
