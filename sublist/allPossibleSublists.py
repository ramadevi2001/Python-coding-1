def allsublist(lst):
    result=[]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            result.append(lst[i:j])
    return result
lst=list(map(int,input('enter the list:').split()))
print(allsublist(lst))


