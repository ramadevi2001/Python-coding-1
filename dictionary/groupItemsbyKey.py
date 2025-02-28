def groupitemsbkey(data):
    
    grouped_items={}
    for key, value in data:
        if key not in grouped_items:
            grouped_items[key]=[]
        grouped_items[key].append(value)
    return grouped_items
data=[('a', 1), ('b', 2), ('a', 3), ('b', 4)]
print(groupitemsbkey(data))
