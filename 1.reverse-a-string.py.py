string=str(input('enter string:'))
reverse=string[::-1]
print('reversed string: ', reverse)

# without using slicing

reversing= ''
for char in range(len(string)-1,-1,-1):
    reversing+=string[char]
print(reversing)

