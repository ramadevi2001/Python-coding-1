def issublist(main,sub):
    if not sub:
        return True
    n,m=len(main),len(sub)
    for i in range(n-m+1):
        if main[i:i+m]==sub:
            return True
    return False
print(issublist([1,2,3,4,5],[1,2,3]))
print(issublist([1,2,3,4,5],[]))
print(issublist([1,2,3,4,5],[1,2,6]))






