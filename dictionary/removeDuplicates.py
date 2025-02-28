def removeDuplicates(dic):
    uniquedict={}
    for key,value in dic.items():
        if value not in uniquedict.values():
            uniquedict[key]=value
    return uniquedict
dic={'a': 1, 'b': 2, 'c': 1, 'd': 3}
print(removeDuplicates(dic))