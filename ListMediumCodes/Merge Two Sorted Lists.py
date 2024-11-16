#without using builtin functions
def  merge_sorted_list(lst1,lst2):
    merged_list=[]
    i, j  = 0, 0
    while i <len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i +=1
        else:
            merged_list.append(lst2[j])
            j +=1
    while i < len(lst1):
        merged_list.append(lst1[i])
        i+=1
    while j < len(lst2):
        merged_list.append(lst2[j])
        j+=1
    return merged_list
lst1 = list(map(int, input('Enter list1 (sorted): ').split()))
lst2 = list(map(int, input('Enter list2 (sorted): ').split()))

merged = merge_sorted_list(lst1, lst2)
print('Merged Sorted List:', merged)

'''
Example Walkthrough:
Given lists:
lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
Merging Steps:
Compare 1 (from lst1) with 2 (from lst2):

1 is smaller, so we append 1 to merged_list and increment i.
merged_list = [1], i = 1, j = 0
Compare 3 (from lst1) with 2 (from lst2):

2 is smaller, so we append 2 to merged_list and increment j.
merged_list = [1, 2], i = 1, j = 1
Compare 3 (from lst1) with 4 (from lst2):

3 is smaller, so we append 3 to merged_list and increment i.
merged_list = [1, 2, 3], i = 2, j = 1
Compare 5 (from lst1) with 4 (from lst2):

4 is smaller, so we append 4 to merged_list and increment j.
merged_list = [1, 2, 3, 4], i = 2, j = 2
Now lst1 is exhausted (i.e., i = 3), but lst2 still has 6:

We append the remaining element from lst2 to merged_list:
merged_list = [1, 2, 3, 4, 5, 6]
'''