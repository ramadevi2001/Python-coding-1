def khtlargest(lst,k):
    return sorted(lst,reverse=True)[k-1] # k-1 is used bec the index is starts from '0'
lst=list(map(int,input('enter lst:').split()))
k= int(input('enter k:'))
print(khtlargest(lst,k))