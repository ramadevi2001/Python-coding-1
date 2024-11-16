def Remove_even(lst):
    odd_num=[]
    for num in lst:
        if num%2!=0:
            odd_num.append(num)
    return odd_num
lst=list(map(int,input('enter the list:').split()))
result=Remove_even(lst)
print('The list of odd numbers:',result)