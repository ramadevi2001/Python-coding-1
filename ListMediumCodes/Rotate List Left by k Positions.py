def move_left_k_positions(lst,k):
    k = k%len(lst)
    rotated_list = lst[k:] + lst[:k]
    return rotated_list
lst=list(map(int,input('enter the list:').split()))
k = int(input('enter k:'))
result= move_left_k_positions(lst,k)
print('rotated the list by k postions : ',  result)

'''
For the list [10, 20, 30, 40, 50] and k = 3:

List: [10, 20, 30, 40, 50]

k: 3

Step 1: Adjust k:

python
Copy code
k = 3 % 5  # k remains 3
Step 2: Slice the list at k = 3:

lst[k:] → [40, 50]
lst[:k] → [10, 20, 30]
Concatenate: [40, 50] + [10, 20, 30] → [40, 50, 10, 20, 30]

Output: The rotated list after 3 positions is [40, 50, 10, 20, 30].
'''