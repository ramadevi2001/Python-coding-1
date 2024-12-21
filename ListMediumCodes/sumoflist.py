def sumoflist(lst):
    sum = 0
    for num in lst:
        sum+= num
    return sum
lst=list(map(int,input('enter the list:').split()))
print(sumoflist(lst))
        

