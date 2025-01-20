def keysStartingwithletter(dic):
    listofkes=[]
    for key in dic:
        if key.startswith(('a','A')):
            listofkes.append(key)
    return listofkes
dic={'apple': 1, 'banana': 2, 'avocado': 3,'App':8}
print(keysStartingwithletter(dic))