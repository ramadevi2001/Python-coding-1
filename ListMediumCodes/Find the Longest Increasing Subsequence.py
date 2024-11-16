def LIS(lst):
    len_lst= [1] * len(lst)
    for i in range(len(lst)):
        for j in range(i):
            if lst[j]<lst[i]:
                len_lst[i]= max(len_lst[i],len_lst[j]+1)
    return max(len_lst)
lst=list(map(int,input('enter the list:').split()))
print('longest increasing subsequence:',LIS(lst))

