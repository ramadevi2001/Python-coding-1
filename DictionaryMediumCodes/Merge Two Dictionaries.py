def merge_dict(dict1,dict2):
    dict3=dict1.copy()
    for key, value in dict2.items():
        if key in dict3:
            dict3[key]+=value
        else:
            dict3[key] = value
    return dict3
import ast # to get the dict from the user 
dict1=ast.literal_eval(input('enter dict1:'))
dict2=ast.literal_eval(input('enter dict2:'))
print(merge_dict(dict1,dict2))


    
