# using for loop
def reversedict(dic):
    reverseddict={}
    for keys, values in dic.items():
        reverseddict[values]=keys
    return reverseddict
dic={'rama':1,'devi':2,'cheruku':3}
print(reversedict(dic))

# using map function

dic={'a':1,'b':2,'c':3}
reverseddict=dict(map(reversed,dic.items()))
print(reverseddict)

#If the keys and values of the dictionary can be extracted as separate lists, 
# you can use the zip() function to create a reversed dictionary.

dic={'Naidu':1,'Ramesh':2}
keys=dic.keys()
values=dic.values()
reverseddict=dict(zip(values,keys))
print(reverseddict)

# using dict comprehension

dic={'apple':1,'banana':2,'orange':3}
revereseddict={value: key for key , value in dic.items() }
print(revereseddict)