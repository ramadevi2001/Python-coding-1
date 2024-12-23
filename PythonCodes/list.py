# largest number in list

lst=list(map(int,input('enter the list:').split()))
largest_number= lst[0] 
for i in lst:
    if i > largest_number:
        largest_number = i
print(largest_number)
# print(max(largest_number)) we will usse max also

# reverse a list

lst=list(map(int,input('enter the list:').split()))
lst.reverse()
print(lst)

# remove duplicates from a list

lst=list(map(int,input('enter the list:').split()))

duplicates=list(set(lst))
print(duplicates)


