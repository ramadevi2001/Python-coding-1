data = {'a': 3, 'c': 1, 'b': 2}
sorted_dict=dict(sorted(data.items(), key= lambda item: item[1])) # index item[1] means values 
print(sorted_dict)
