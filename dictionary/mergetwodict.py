# update , modifies the original dict1
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)

# using ** operator it unpacks the items , and for merging combine them
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
mergedDict={**dict1,** dict2}
print(mergedDict)

# using the | (union) operator

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
mergedDict=dict1|dict2
print(mergedDict)