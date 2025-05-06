def firstnonrepeating(str):
    s_low=str.lower()
    for char in s_low:
        if s_low.count(char)==1:
            return char
    return None
str='samanthas'
print(firstnonrepeating(str))
    
    