def duplicate_lsit(lst):
    seen=set()
    duplicate_list=[]
    for num in lst:
        if num in seen:
            if num not in duplicate_list:
                duplicate_list.append(num)
        else:
            seen.add(num)


    return duplicate_list
lst=list(map(int,input('enter the list:').split()))
result=duplicate_lsit(lst)
print('duplicate list:',result)
