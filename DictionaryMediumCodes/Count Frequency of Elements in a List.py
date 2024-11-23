def count_frequency(lst):
    count={}
    for i in lst:
        count[i]=count.get(i,0)+1
    return count
lst=list(map(int,input('enter a list:').split()))
print(count_frequency(lst))

# using the counter from collections

from collections import Counter
lst=list(map(int,input('enter a list:').split()))
print(dict(Counter(lst)))