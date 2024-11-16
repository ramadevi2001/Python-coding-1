def missing_smallest_positive_integer(lst):
    pos_list=[]
    for num in  lst:
        if num>0:
            pos_list.append(num)
    pos_list.sort()

    expected=1
    
    for i in pos_list:
        if i==expected:
            expected+=1
        elif i > expected:
            return expected
    return expected
lst=[2,5,1,-6,7]
print(missing_smallest_positive_integer(lst))


